# UDP编程

# TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
# 虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。


# https://www.cnblogs.com/duanxz/p/5127561.html
'''
TCP与UDP基本区别
1.基于连接与无连接
2.TCP要求系统资源较多，UDP较少；
3.UDP程序结构较简单
4.流模式（TCP）与数据报模式(UDP);
5.TCP保证数据正确性，UDP可能丢包
6.TCP保证数据顺序，UDP不保证
　　
UDP应用场景：
1.面向数据报方式
2.网络数据大多为短消息
3.拥有大量Client
4.对数据安全性无特殊要求
5.网络负担非常重，但对响应速度要求高

具体编程时的区别
1.socket()的参数不同
2.UDPServer不需要调用listen和accept
3.UDP收发数据用sendto / recvfrom函数
4.TCP：地址信息在connect / accept时确定
5.UDP：在sendto / recvfrom函数中每次均需指定地址信息
6.UDP：shutdown函数无效
'''


# 我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口

import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 9999))

# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据


print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
    time.sleep(1)

# recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
# 注意这里省掉了多线程，因为这个例子很简单。
