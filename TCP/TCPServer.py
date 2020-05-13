from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)#创建一个TCP套接字（欢迎套接字）
serverSocket.bind(('', serverPort))#将端口和Socket绑定
serverSocket.listen(1)#监听TCP连接请求，并设置最大连接数为1
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()#收到TCP连接请求，创建新的连接套接字（连接套接字）
    sentence = connectionSocket.recv(1024).decode()#解析数据
    print('Received data is ' + sentence)
    capitalizedSentence = sentence.upper()#处理数据
    connectionSocket.send(capitalizedSentence.encode())#发送处理后的数据
    connectionSocket.close()#关闭连接套接字
