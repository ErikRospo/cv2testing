
import cv2 as cv
def main(image):
    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "Laplace Demo"
    src=image
    src = cv.GaussianBlur(src, (3, 3), 0)
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
    abs_dst = cv.convertScaleAbs(dst)
    return abs_dst