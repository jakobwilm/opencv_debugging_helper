#include <iostream>

#include <opencv2/opencv.hpp>

#include <QImage>
#include <QPixmap>

using namespace std;

int main(int argc, char *argv[]) {

  cv::Size size(34, 23);

  //    cv::Mat mat = cv::imread("tex.jpg");

  cv::Mat mat(4, 3, CV_32FC3);
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 3; j++)
      mat.at<cv::Vec3f>(i, j) = cv::Vec3f(i + j, i + j + 4, i + j + 8);

  cv::Mat mat2 = mat.clone();

  QImage im("tex.jpg");

  QString string("hello");

  return 0;
}
