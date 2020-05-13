from socket import *

from pip._vendor.distlib.compat import raw_input

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)#创建套接字
message = raw_input('Input lower case sentence:')#创建要发送的信息
clientSocket.sendto(message.encode(), (serverName, serverPort))#将待发送信息放进套接字中并发送
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)#等待返回的信息
print(modifiedMessage.decode())
clientSocket.close()#关闭套接字链连接