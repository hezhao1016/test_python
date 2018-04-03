# struct

# struct的pack函数把任意数据类型变成bytes
import struct
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
b = struct.pack('>I', 10240009)
print(b)

# unpack把bytes变成相应的数据类型
str = struct.unpack('>I', b)
print(str)
str1 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')  # >IH表示，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
print(str1)

