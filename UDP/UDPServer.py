from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)#创建服务套接字
serverSocket.bind(('', serverPort))#将服务套接字和端口绑定
print('The server is ready to receive:')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)#套接字等待分组到达
    print('The received message is ' + message)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)#返回处理后的信息