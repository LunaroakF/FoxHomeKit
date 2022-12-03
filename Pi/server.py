from dataclasses import replace
import threading
import socket
import os
import time


def outputLog(msg):
    nowtime = "["+time.strftime("%Y-%m-%d %H:%M:%S")+"]"
    print(nowtime+msg)

def Wificl():
    while True:
        try:
            server=socket.socket()
            server.bind(("192.168.0.114",2500))
            server.listen() #监听
            outputLog("Listener started.")
            conn,addr=server.accept()
            #print(conn,addr)
            outputLog("Controller connected.")
            data=conn.recv(128)
            maindata=str(data)
            datalist=maindata.split("'")
            maindata=datalist[1]
            outputLog("Recived data:"+maindata)
            if maindata=="LED1ON":
                SendData("192.168.0.121","LightON")
            if maindata=="LED1OFF":
                SendData("192.168.0.121","LightOFF")
            if maindata=="ALLON":
                SendData("192.168.0.121","LightON")
            if maindata=="ALLOFF":
                SendData("192.168.0.121","LightOFF")
            if maindata=="Toggle":
                SendData("192.168.0.121","Toggle")
            conn.close()
        except:
            #outputLog("error1")
            conn.close()
            
def SendData(IP,send_data):
    outputLog("Trying to send Command to device.")
    port = 2005  # 设置端口号
    tcpclient = socket.socket()  # 创建TCP/IP套接字
    tcpclient.connect((IP, port))  # 主动初始化TCP服务器连接
    outputLog("Command has been sent to device.")
    tcpclient.send(send_data.encode('UTF-8','strict'))  # 发送TCP数据
    #info = tcpclient.recv(1024).decode()
    #print("接收到的内容：", info)
    tcpclient.close()


t_Wificl = threading.Thread(target=Wificl)
t_Wificl.start()
