from machine import Pin
import socket
import time
import WIFIConnect


IP="192.168.0.121"  #设备的内网IP，在路由器或交换机中给与固定IP
Port=2005  #监听的端口
LED = Pin("LED", Pin.OUT)#板载LED
RELAY = Pin(28, Pin.OUT)#继电器
RELAY.value(1)
LED.value(1)
print("链接WIFI...")
WIFIConnect.ConnectWIFI('LunaroakF','19645277')
LED.value(0)
def ProcessData(data):
    if data=="LightON":
        RELAY.value(0)
    if data=="LightOFF":
        RELAY.value(1)
    if data=="Toggle":
        RELAY.toggle()

def Wificl():
    while True:
        try:
            server=socket.socket()
            server.bind((IP,Port))
            server.listen() #监听
            print("监听已开始")
            conn,addr=server.accept()
            #print(conn,addr)
            print("用户已连接")
            data=conn.recv(128)
            maindata=str(data)
            datalist=maindata.split("'")
            maindata=datalist[1]
            print("用户数据:"+maindata)
            ProcessData(maindata)
            conn.close()
        except:
            #print("error1")
            conn.close()

Wificl()
