import cv2
import OpenCV.MotionDetection.utils as utils

"""

Motion detection with IP Camera

"""

url = ''
cap = cv2.VideoCapture(url)

window_size = {'obtained': False, 'wt': 0, 'ht': 0}
WIN_NAME = 'Mobile Capture'

prev_rgb_arr = []  # For distributed step detection
prev_rgb = []  # For area detection

capture_count = 1

DETECTION_SQUARE_SIZE = 100  # For distributed step detection
DETECTION_STEP = 40  # For area detection
DETECTION_OFFSET = 5  # The change in RGB needed to register as a motion
CAPTURE_FILE_PATH = 'MotionDetection/captures'
FILE_NAME = 'MotionCapture'
EXTENSION = 'jpg'

while 1:
    ret, frame = cap.read()

    if ret:
        if not window_size['obtained']:  # Obtain window information if not already obtained
            window_size['ht'], window_size['wt'] = frame.shape[:2]
            window_size['obtained'] = True

        utils.draw_detection_step(frame, DETECTION_STEP, window_size)  # Draw the distributed detection points

        cv2.imshow(WIN_NAME, frame)  # Show the live video feed from IP Camera

        # Get the RGB values of every detection point and call this the current frame
        curr_rgb_arr = utils.all_rgb_step(frame, DETECTION_STEP, window_size)

        # If the previous array or RGB values is not empty and a motion RGB change has been detected
        if prev_rgb_arr and utils.check_image_array_change(prev_rgb_arr, curr_rgb_arr, DETECTION_OFFSET):
            # Print capture number
            print(f'Movement detected {capture_count}')

            # Write the current frame to computer
            cv2.imwrite(f'{CAPTURE_FILE_PATH}/{FILE_NAME}{capture_count}.{EXTENSION}', frame)

            # Iterate capture count
            capture_count += 1

        # Set previous RGB array to current
        prev_rgb_arr = curr_rgb_arr

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
