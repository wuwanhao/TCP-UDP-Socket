from socket import *

from pip._vendor.distlib.compat import raw_input

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)#创建套接字
clientSocket.connect((serverName, serverPort))#跟服务端建立TCP连接
sentence = raw_input('Input lower case sentence:')
clientSocket.send(sentence.encode())#发送内容
modifiedSentence = clientSocket.recv(1024)#等待服务端传回的数据，缓存长度为1024
print('From server: ', modifiedSentence.decode())
clientSocket.close()#关闭套接字，即关闭了TCP连接