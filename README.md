# Simple Mac manubar item with quick access to my security cameras and smart switch toggles.

![Screenshot](Shot.png)

Dependencies for the cameras:
- python
- rumps by [jaredks](https://github.com/jaredks/rumps)
- [OpenCV-python](https://pypi.org/project/opencv-python/)

See the simple script view_ipcam.py to set up the camera urls.
See mbipc.py for the straightforward rumps bits - very intuitive.

Dependencies for the switch toggles:
- tuyapi by [codetheweb](https://github.com/codetheweb/tuyapi)

See ToggleCoffeeMaker.js for an example of toggling a tuya wifi switch on/off. 
Note you need the key/id for each device.
