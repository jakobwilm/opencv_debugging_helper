# Opencv Debugging Helper
Debugging helper for OpenCV in QtCreator. 

Developed and tested for OpenCV 3.X, QtCreator 4.5 with GDB built against Python 3.

Note that QtCreator 4.5 ships with a (very) rudimentary debugging helper for cv::Mat.

This was created because none of the available projects that I could find currently work with these versions of QtCreator and Python. A future goal is to enable visual debugging of cv::Mat.

## Installation 
Add this file to "Options->Debugger->Locals & Expressions->Extra Debugging Helpers" (from QtCreator 4.x)

In QtCreator 3.x, put the following line in "Additional Startup Commands"
python exec(open("/path/to/opencv_debugging_helper.py").read())

## Thanks
The code is modified and based on the following resources:
[https://github.com/FSund/debugginghelpers/blob/master/armadillo.py]
[https://github.com/geordi/qtcreator-debugging-helpers]
[http://dtmoodie.blogspot.dk/2015/02/getting-image-watch-like-debugging-in.html]
[https://github.com/dtmoodie/GDB-ImageWatch]