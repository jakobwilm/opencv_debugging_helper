QT += core gui
TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle

SOURCES += main.cpp

unix:!macx {
    CONFIG += link_pkgconfig
    PKGCONFIG += opencv4
}
