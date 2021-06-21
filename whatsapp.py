# code to send whatsapp message

import pywhatkit
import time

def whatsapp(msg):
    curr_time=time.ctime()
    curr_time=curr_time.split(" ")
    cur=curr_time[3].split(':')
    print(type(cur[0]))
    pywhatkit.sendwhatmsg("+91xxxxxxxxxx",msg,int(cur[0]),int(cur[1])+1)
