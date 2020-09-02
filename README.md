# IPCamMotionDetection
Detect motion and capture it with an IP Camera

# Usage
- `pip install opencv-python` and run `IPCam.py`
- Install [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_CA), run the app, and input the IPv4 string given to you by the app.
- Specify detection sensitivity inputs, file path, and you're done.

# Executable
- With Pyinstaller, the compiled .exe comes to 40MB alone and 28MB with UPX compression. I'm trying to the reduce the size even more so that it may be installed at a practical size.
