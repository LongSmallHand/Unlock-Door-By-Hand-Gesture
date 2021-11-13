import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract.exe'

def pwd_scan(img):
    # img =cv2.imread('WORD.png')
    # image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)
    with open("pwd.txt", 'w', encoding='utf-8') as f:
        f.write(text)
    f.close()
    # cv2.imshow('Result', img)
    # cv2.waitKey(0)
