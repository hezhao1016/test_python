# IMAP | 通过IMAP收邮件

# SMTP是用于发送电子邮件的协议，而IMAP规定如何与电子邮件服务提供商的服务器通信，取回发送到你的电子邮件地址的邮件
# Python带有一个imaplib模块，还有第三方的imapclient、pyzmail模块

# POP3和IMAP协议的区别
# 虽然这两个协议都是从邮件服务器那里下载邮件到本地的协议，但是不同的是IMAP提供跟邮件服务器的双向通信，也即在客户端所作的更改会反馈给服务器端，跟服务器端形成同步（例如删除邮件，创建文件夹等等的操作）。
# 而POP3是单向通信的，即下载邮件到本地就算了，所作的更改都只是在客户端，不会反映到服务器端。所以使用IMAP协议也会更便捷，体验更好，更可靠。


import imaplib
import email
from email.header import decode_header
from email.utils import parseaddr

username = 'xxx@foxmail.com'  # 账户
password = '请输入密码'  # 密码
imap_server = 'imap.qq.com'  # IMAP服务器地址

# 登陆邮箱

# conn = imaplib.IMAP4(host=imap_server, port=143)
server = imaplib.IMAP4_SSL(host=imap_server, port=993)  # 加密连接
print('已连接服务器...')
server.login(username, password)
print('已登录...')

# 打印所有文件夹
resp, mails = server.list()
print(mails)

# 选择邮箱中的一个文件夹,默认值是INBOX
result, message = server.select()
print(result, message)

# 搜索匹配的邮件，第一个参数是字符集，None默认就是ASCII编码，第二个参数是查询条件，这里的ALL就是查找全部。
# 该函数返回的是字符数组，我们只需要数组的第一个元素，数组的第一个元素是邮件的编号，并且按接收时间按升序排序并且中间用空格隔开。
# 例如[‘1 2 3 4 5 6 7 8 9 10 ……’]，所以现在我们只需把这些用空格隔开的数分离开来放到一个新的数组就OK了
type, data = server.search(None, 'ALL')
print(type, data)

newlist = data[0].split()
print(newlist)

# 然后可以调用fetch()方法来取回邮件，不过取回来的邮件是一堆乱七八糟的东西，我们要把我们取回的邮件用email库来进行一些处理。
#如果我们要取回第一封邮件可以把newlist[0]传递给fetch()
type, data = server.fetch(newlist[0], '(RFC822)')
print(type, data)

# 解析出Message对象
msg = email.message_from_string(data[0][1].decode('utf-8'))

# 关闭资源
server.close()
server.logout()



# 递归地打印出Message对象的层次结构
# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
# decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。


# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

# 把上面的代码整理好，我们就可以来试试收取一封邮件。先往自己的邮箱发一封邮件，然后用浏览器登录邮箱，看看邮件收到没，如果收到了，我们就来用Python程序把它收到本地

print_info(msg)

