'''
This a demo python code which converts an image to it's grayscale image.
It uses opencv-python library to do this.
'''
import cv2
image = cv2.imread("trialIMG.jpg") # Please give appropriate path to the image to be converted
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert image to grayscale
inverted_image = 255 - gray_image #Invert the image for best results
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0) # Create pencil sketch
# Open Image
cv2.imshow("Real Image", image)
cv2.imshow("Pencil Sketch of the given image", pencil_sketch)
cv2.waitKey(0)