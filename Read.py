import enum
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract.exe'

# img = cv2.imread('test1.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# height, width,_ = img.shape

# Character
# box = pytesseract.image_to_boxes(img)
# for b in box.splitlines():
#     b = b.split()
#     # print(b)
#     x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x, height - y), (w, height - h), (0,0,255), 1)
#     cv2.putText(img, b[0], (x, height - y - 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,225), 2)

# Word
# data = pytesseract.image_to_data(img)
# for x, b in enumerate(data.splitlines()):
#     if x != 0:
#         b = b.split()
#         # print(b)
#         if len(b) == 12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x, y), (w+x, h+y), (0,0,255), 1)
#             cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,225), 2)
# cv2.imshow('Result',img)
# cv2.waitKey(0)

def read(img):
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    height, width,_ = img.shape
    # Character
    box = pytesseract.image_to_boxes(img)
    for b in box.splitlines():
        b = b.split()
        # print(b)
        x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, height - y), (w, height - h), (0,0,255), 1)
        cv2.putText(img, b[0], (x, height - y - 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,225), 2)
        cv2.imshow('Result',img)
        cv2.waitKey(0)