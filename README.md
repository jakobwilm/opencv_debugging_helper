# Opencv Debugging Helper
Debugging helper for OpenCV in QtCreator. 

Developed and tested for OpenCV 3.X, QtCreator 4.5.2 (Ubuntu 18.04) with GDB built against Python 3.

Note that QtCreator 4.5 ships with a (very) rudimentary debugging helper for cv::Mat. If this debugging helper is successfully loaded, it will override the built-in.

This was created because none of the available projects that I could find currently work with these versions of QtCreator and Python. A future goal is to enable visual debugging of cv::Mat.

## Installation 
Add this file to "Options->Debugger->Locals & Expressions->Extra Debugging Helpers" (from QtCreator 4.x)

## Thanks
The code is modified and based on the following resources:
[https://github.com/FSund/debugginghelpers/blob/master/armadillo.py]
[https://github.com/geordi/qtcreator-debugging-helpers]
[http://dtmoodie.blogspot.dk/2015/02/getting-image-watch-like-debugging-in.html]
[https://github.com/dtmoodie/GDB-ImageWatch]
