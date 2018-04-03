# imapclient & pyzmail | Python IMAP 协议的第三方模块

# 在命令行下通过pip安装：
# $ pip install imapclient
# $ pip install pyzmail
# 如果遇到Permission denied安装失败，请加上sudo重试。

import imapclient
import pprint

username = 'xxx@foxmail.com'  # 账户
password = '请输入密码'  # 密码
imap_server = 'imap.qq.com'  # IMAP服务器地址


# 创建一个IMAPClient对象，大多数邮件提供商要求SSL加密，传入ssl = True关键字参数
imapObj = imapclient.IMAPClient(imap_server, ssl=True)

# 取得IMAPClient后，调用login()方法，传入用户名和密码字符串
imapObj.login(username, password)


# 搜索邮件：
# 1、选择需要搜索的文件夹；
# 2、必须调用IMAPClient对象的search()方法，传入IMAP搜索关键词字符串
# 3、选择文件夹：几乎每一个帐户都默认有一个INBOX文件夹，但是也可以调用IMAPClient对象的list_folders()方法，获取文件夹列表。list_folders()方法返回一个元组的列表，每一个元组包含一个文件夹信息

pprint.pprint(imapObj.list_folders())

# 要选择一个文件夹进行搜索，就调用select_folder()方法，传入该文件夹的名称字符串
imapObj.select_folder('INBOX', readonly=True)

# 可以忽略select_folder()返回值，当搜索的文件夹不存在时。Python抛出imap.error异常
# readonly = True关键字参数可以防止你在随后的方法调用中，不小心更改或删除该文件夹中的任何电子邮件


# 执行搜索：文件夹选中后就可以调用IMAPClient对象的search()方法搜索电子邮件
# search()方法的参数是一个字符串列表，每一个格式化为IMAP的搜索键

# IMAP搜索键：
#
# 'ALL'：返回该文件夹中的所有邮件。如果你请求一个大文件夹中的所有信息，可能会遇到imaplib的大小限制
#
# 'BEFORE/ON/SINCE date'：分别返回给定的date之前、当天、之后IMAP服务器接受的消息，日期格式必须是05-Jul-2017
# 此外，虽然“SINCE 05-Jul-2017”将匹配7月5日当天和之后的消息，但是“BEFORE 05-Jul-2017”仅匹配7月5日之前的消息，不包括7月5日当天
#
# 'SUBJECT/BODY/TEXT string':分别返回string出现在主题、正文、主题或正文中的消息，如果string中有空格，就是用双引号
#
# 'FROM/TO/CC/BCC string':返回所有信息，其中string分别出现在“from”邮件地址、“to”邮件地址、“cc”（抄送）地址、或“bcc”（密件抄送）地址
# 如果string中有多个邮件地址，就是用空格将他们分割开，并使用双引号
#
# 'SEEN/UNSEEN'：分别返回包含和不包含\Seen标记的所有信息。如果电子邮件已经被fetch()方法调用访问，或者你曾在电子邮件程序中或网络浏览器中点击过它，
# 就会有\Seen标记，比较常用的说法是“已读”而不是“已看”
#
# 'ANSWERED/UNANSERED':分别返回包含和不包含\Answered标记的所有信息，如果消息已答复就会有\Answered标记
#
# 'DELERED/UNDELETED':分别返回包含和不包含\Deleted标记的所有信息，用delete_messages()方法删除的邮件就会有\Deleted标记，直到调用expunge()方法才
# 会永久删除
#
# 'DRAFT/UNDRAFT'：分别返回包含和不包含\Draft标记的所有信息，草稿邮件通常保存在单独的草稿文件夹中，而不是收件箱
#
# 'FLAGGED/UNFLAGGED'：分别返回包含和不包含\Flagged标记的所有信息，这个标记通常用来标记电子邮件的“重要”或“紧急”
#
# 'LARGER/SMALLER N'：分别返回大于或小于N个字节的所有信息
#
# 'NOT search-key':返回搜索键不会返回的那些信息
#
# 'OR search-key1 search-key2':返回符合第一个或者第二个搜索键的信息


# imapObj.search(['all'])
# imapObj.search(['ON 05-Jul-2017'])
# imapObj.search(['SINCE 01-Jul-2017', 'BEFORE 05-Jul-2017'])
# imapObj.search(['OR FROM alie@qq.com FROM habo@qq.com'])


# search不返回电子邮件本身，而是返回邮件的唯一整数ID（UID），然后可以将这些UID传入fetch(),获得邮件内容
UIDS = []
UIDS = imapObj.search(['all'])

# 大小限制：
# 如果搜索匹配大量的电子邮件，Python可能会抛出imap.error：got more than 10000 bytes的异常，必须断开重连IMAP服务器
# 可以调整限制的字节数

# import imaplib
# imaplib._MAXLINE = 10000000


# 取邮件并标记为已读
# 获取到UID的列表后，就可以调用IMAPClient对象的fetch()方法，获得实际的电子邮件内容
# UID列表是fetch()函数的第一个参数，第二个参数应该是['BODY[]'],它告诉fetch()下载UID列表中指定电子邮件的所有正文内容

rawMessages = imapObj.fetch(UIDS, ['BODY[]'])
pprint.pprint(rawMessages)


# 打印结果：
# 返回值是消息的嵌套字典，其中以UID作为键，每条消息同业也保存为一个字典，包含两个键'BODY[]'和'SEQ'
# 'BODY[]'映射到电子邮件的实际正文；'SEQ'键是序列号
# 形如：｛UID：｛'BODY[]':邮件正文内容,'SEQ'：序列号｝｝
#
# 'BODY[]'键中的消息内容是相当难以理解的，这种格式被称为RFC822，专为IMAP服务器读取设计的，稍后通过pyzmail模块解析
#
# 如果选择一个文件夹来搜索，需要用关键字readonly = True参数来调用函数select_folder(),这样做可以防止意外删除电子邮件，
# 但是也意味着用fetch()方法获取邮件内容，他们不会被标记为已读
#
# 如果确实需要在获取的同时标记为已读，可以将readonly = False传递给select_folder()方法，即所选文件夹处于只读模式
# imapObj.select_folder('INBOX',readonly = False)


# 从原始信息中获取电子邮件地址
# 通过pyzmail模块解析这些原始信息，返回一个PyzMessage对象返回，是邮件的正文、主题、收件人、发件人以及其他字段信息
#导入pyzmail模块后，调用pyzmail.PeekMessage.factory()函数，创建一个PyzMessage对象
import pyzmail
messageObj = pyzmail.PyzMessage.factory(rawMessages[1369][b'BODY[]'])


# get_subject()方法将主题返回为一个简单的字符串，get_addresses()针对传入的字段（参数是'from','to','cc','bcc'），返回一个地址的元组列表
# 每一个元组包含两个字符串，第一个是与该电子邮件地址关联的名称，第二个是电子邮件地址本身，如果请求的字段中没有地址，返回一个空的列表
print(messageObj.get_subject())
print(messageObj.get_addresses('from'))
print(messageObj.get_addresses('to'))
# messageObj.get_addresses('cc')
# messageObj.get_addresses('bcc')



# 从原始消息中获取正文
# 电子邮件可以是纯文本、HTML或者两者混合
# 纯文本电子邮件只包含文本，而HTML电子邮件可以有颜色、字体、图像、和其他功能
# 如果电子邮件是纯文本，PyzMessage对象会将html_part属性设为None，同样，当邮件只有HTML，PyzMessage对象会将text_part属性设置为None
# 否则，text_part或者html_part将有一个get_payload()方法，将电子邮件的正文返回为bytes数据类型，但是这仍然不是我们可以使用的字符串，
# 最后一步对get_payload()返回的bytes值调用decode()方法。decode()方法接受一个参数：这条消息的字符编码，保存在text_part.charset或html_part.charset属性中

if messageObj.text_part != None:
    messageConten = messageObj.text_part.get_payload().decode(messageObj.text_part.charset)
    pprint.pprint(messageConten)
elif messageObj.html_part != None:
    messageConten = messageObj.html_part.get_payload().decode(messageObj.html_part.charset)
    pprint.pprint(messageConten)
else:
    pass



# 删除电子邮件
# 要删除电子邮件，就需要想IMAPClient对象的delete_messages()方法传入一个消息的UID列表，这为电子邮件加上了\Deleted标记
# 调用expunge()方法，将永久删除当前选中的文件夹中的带\Deleted标志的所有电子邮件
# imapObj.select_folder('INBOX', readonly=False)
# UIDs = imapObj.search('ON 09-Jul-2017')
#
# imapObj.delete_messages(UIDs)
# imapObj.expunge()


# 从IMAP服务器断开，调用IMAPClient对象的logout()方法
imapObj.logout()