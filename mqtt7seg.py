from machine import Pin
import time
import network 
from umqtt.simple import MQTTClient as umqtt
def allOFF():
    for i in led:
        i.value(1)
def allON():
    for i in led:
        i.value(0)
def show(num):
    for i in range(7):
        led[i].value(arrSeg[num][i])
def get_msg(topic,msg):
    msg1=str(msg).replace('b','')
    msg1=eval(msg1)
    a= int(int(msg1)/10)
    if a>9:
        a=9
    elif a<0:
        a=0
    print(a)
    show(a)
    return msg1

arrSeg = [[0,0,0,0,0,0,1],[1,0,0,1,1,1,1],[0,0,1,0,0,1,0],[0,0,0,0,1,1,0],[1,0,0,1,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,1,1,0,1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0]]
pwr= Pin(13, Pin.OUT)
A = Pin(19, Pin.OUT)
B = Pin(21, Pin.OUT)
C = Pin(12, Pin.OUT)
D = Pin(22, Pin.OUT)
E = Pin(23, Pin.OUT)
F = Pin(18, Pin.OUT)
G = Pin(5, Pin.OUT)
pwr.value(1) #給共陽極通電
led=[A,B,C,D,E,F,G]
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if wlan.isconnected():
    wlan.disconnect()
else:
    wlan.connect('wlan','passwd')
    for i in range(20):
        print('try to connect wifi in {}s'.format(i/2))
        time.sleep(0.5)
        if wlan.isconnected():
            break          
    if wlan.isconnected():
        print('WiFi connection OK!')
        print('Network Config=',wlan.ifconfig())
    for i in range(3):
        allON()
        time.sleep(0.5)
        allOFF()
        time.sleep(0.5)
    else:
        print('WiFi connection Error') 
    
mqClient0 = umqtt('xiang','140.127.220.208')
mqClient0.connect()
mqClient0.set_callback(get_msg)
mqClient0.subscribe('XIANGYU')
while True:
    mqClient0.check_msg()
    time.sleep(0.5)


