# Opencv Debugging Helper
Debugging helper for OpenCV in QtCreator. 

Developed and tested for OpenCV 4.X, QtCreator 10.0 (Ubuntu 22.04) with GDB built against Python 3.

Note that QtCreator ships with a rudimentary debugging helper for cv::Mat. If this debugging helper is successfully loaded, it will override the built-in.
Note that visualization of a cv::Mat is currently not possible on most platforms due to a long standing bug in QtCreator: https://bugreports.qt.io/browse/QTCREATORBUG-21233

This was created because none of the available projects that I could find currently work with these versions of QtCreator and Python. 

## Installation 
Add this file to "Options->Debugger->Locals & Expressions->Extra Debugging Helpers" (from QtCreator 10.x)
When using CDB as debugger backend, you can enable the Python dumper by selecting Edit > Preferences > Debugger > CDB > Use Python dumper.

## Thanks
The code is inspired and partly based on the following resources:
[https://github.com/FSund/debugginghelpers/blob/master/armadillo.py]
[https://github.com/geordi/qtcreator-debugging-helpers]
[http://dtmoodie.blogspot.dk/2015/02/getting-image-watch-like-debugging-in.html]
[https://github.com/dtmoodie/GDB-ImageWatch]
