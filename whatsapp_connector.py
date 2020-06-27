from chat_bot import chatbot
from whatsapp_utils import AutoWhatsApp
import time


MESSAGE_TXT = """THis is a multi-line msg
line 1
line 2
line 3"""


whatsbot = AutoWhatsApp("/home/parashar/.config/google-chrome/Default")


print("please select group/contact to get messages from")
time.sleep(10)

while True:
    try:
        msg = whatsbot.chk_new_message()
        if msg:
            response = chatbot.get_response(msg)
            print("{}->{}".format(msg, response))
            whatsbot.write_text_message("{} -chatbot".format(response))
        else:
            time.sleep(5)
    except:
        print("crashed")
        time.sleep(5)

