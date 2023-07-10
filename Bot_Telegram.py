import telegram
import cv2
import os
def bot_message():

    try:
        #Use this token to access the HTTP API:
        notify = telegram.Bot("5012281775:AAH0bp5Wx5tBwRtCQfP4SzoyRI5EdKBjbtw")
        #Read file 
        f1 = open("PassLog/Log.txt", 'r+', encoding='UTF-8')
        data1 = f1.read()
        message1 = "{}".format(data1)
        notify.send_message(chat_id="-795707678", text=message1, parse_mode='Markdown')
    except Exception as ex:
        print(ex)
        
def bot_photo():
    try:
        notify = telegram.Bot("5012281775:AAH0bp5Wx5tBwRtCQfP4SzoyRI5EdKBjbtw")
        notify.send_photo(chat_id="-795707678", photo = open('Fail/human.png', 'rb'), caption = "Someone try to open the door! Do you know this person?")
    except Exception as ex:
        print(ex)
