def thresh_callback(val,src,color):
    threshold = val
    # Detect edges using Canny
    canny_output = cv2.Canny(src, threshold, threshold * 2)
    # Find contours
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Draw contours
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        cv2.drawContours(drawing, contours, i, color, 2, cv2.LINE_8, hierarchy, 0)
    # Show in a window
    return drawing
def GetContours(image,thresh,color=(0,255,0)):
    src_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    src_grey = cv2.blur(src_grey, (3,3))
    thresh_callback(thresh,src_grey,color)