from cv2 import rectangle, circle

"""

Useful functions for motion detection

"""


def all_rgb_step(image, step, window_size):
    """Simply returns all the RGB values from pixels on an interval step and returns as a 2D list"""
    image_array = []

    for x in range(0, window_size['wt'], step):
        for y in range(0, window_size['ht'], step):
            image_array.append(image[y, x])

    return image_array


def check_image_array_change(prev, curr, offset):
    """Check if one 2D RGB list is within some +/- offset of another"""
    for i in range(len(prev)):
        if check_rgb_change(prev[i], curr[i], offset):
            return True

        else:
            return False


def check_rgb_change(prev, curr, offset):
    """Check if one RGB value is within some +/- offset of another"""
    for i in range(3):
        if not (curr[i] - offset <= prev[i] <= curr[i] + offset):
            return True

        else:
            return False


# Functions for visualization
def draw_detection_step(frame, step, window_size):
    """Draw the distribution of detection pixels on an interval step"""
    for x in range(0, window_size['wt'] + 1, step):
        for y in range(0, window_size['ht'] + 1, step):
            circle(frame, (x, y), 1, (0, 0, 0), 1)


def draw_detection_square(frame, square_size, window_size):
    """Draw the square of pixels used for detection (inefficient)"""
    p1 = window_size['wt'] // 2 - square_size // 2, window_size['ht'] // 2 - square_size // 2
    p2 = window_size['wt'] // 2 + square_size // 2, window_size['ht'] // 2 + square_size // 2
    rectangle(frame, p1, p2, (0, 0, 0))
