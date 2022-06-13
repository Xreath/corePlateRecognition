
import cv2
import pytesseract

box = cv2.imread("detections/video/frame_60/plate_2.png")
gray = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)

text = pytesseract.image_to_string(gray, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
print(text)
print(len(text))

