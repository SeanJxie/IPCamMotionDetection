# IPCamMotionDetection
Detect motion and capture it with an IP Camera.

# Usage
- With Python and `pip` installed, `pip install opencv-python` and run `IPCam.py` with any IDE (with the executable found below, simply run the application).
- Provided that you are on the same wifi network as your mobile device, install [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_CA), run the app, and input the IPv4 string given to you by the app.
- Specify detection inputs, file path, and you're good to go!

# Executable
- With Pyinstaller, the compiled `.exe` file comes to 40MB alone and 28MB with UPX compression which still isn't the smallest program. I'm trying to the reduce the size even more so that it may be installed at a practical size. If you really want to download the program executable: [here](https://www.dropbox.com/s/3dohe31xzaq7i3h/IPCam.exe?dl=0).

# Development
- New detection algorithm uses frame difference rather than RGB comparison which means more precise, accurate, and faster motion detection.
