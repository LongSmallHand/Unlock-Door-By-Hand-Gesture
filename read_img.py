import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2

Path = "Image"
myImage = os.listdir(Path)
core = "password_record.png"
if core in myImage:
    image = cv2.imread('Image/password_record.png', cv2.IMREAD_UNCHANGED)
else:
    image = cv2.imread('empty_pw/blank.png', cv2.IMREAD_UNCHANGED)
    
cs_config = r'-c tessedit_char_whitelist=ABCDEFGH123456789 --psm 7 --oem 3'
image_text = pytesseract.image_to_string(image, lang='eng', config=cs_config)



