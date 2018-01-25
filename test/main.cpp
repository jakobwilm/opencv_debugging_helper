#include <iostream>

#include <opencv2/opencv.hpp>

#include <QImage>

using namespace std;

int main(int argc, char *argv[])
{

    cv::Size size(34, 23);

    cv::Mat mat(3, 2, CV_32FC3); //= cv::imread("tex.jpeg");

    for(int i=0; i<3; i++)
        for(int j=0; j<2; j++)
            mat.at<cv::Vec3f>(i,j) = cv::Vec3f(i+j, i+j+ 4, i+j+ 8);

    cv::Mat mat2 = mat.clone();

    QImage im("tex.jpeg");


    return 0;
}
