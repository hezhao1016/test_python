'''
https://blog.csdn.net/shijichao2/article/details/51228408

python-qrcode是个用来生成二维码图片的第三方模块，依赖于 Pillow、Image 模块。

pip install qrcode
pip install pillow
pip install Image

L级：约可纠错7%的数据码字
M级：约可纠错15%的数据码字
Q级：约可纠错25%的数据码字
H级：约可纠错30%的数据码字

生成二维码的步骤：
1. 创建QRCode对象
2. add_data()添加数据
3. make_image()创建二维码（返回im类型的图片对象）
4. 自动打开图片，im.show()

'''


import qrcode

# 自动打开一张生成好的二维码图片
# qrcode.run_example()


# 1：简单调用
# data = 'http://write.blog.csdn.net/'
# img_file = r'../../files/py_qrcode1.png'
#
# img = qrcode.make(data)
# # 图片数据保存至本地文件
# img.save(img_file)
# # 显示二维码图片
# img.show()


# 2：生成参数
data = 'http://write.blog.csdn.net/'
img_file = r'../../files/py_qrcode2.png'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
img.save(img_file)
img.show()


'''
QRCode参数详细说明：

version: 一个整数，范围为1到40，表示二维码的大小（最小值是1，是个12×12的矩阵），如果想让程序自动生成，将值设置为 None 并使用 fit=True 参数即可。
error_correction: 二维码的纠错范围，可以选择4个常量： 
ERROR_CORRECT_L 7%以下的错误会被纠正 
ERROR_CORRECT_M (default) 15%以下的错误会被纠正，默认值
ERROR_CORRECT_Q 25 %以下的错误会被纠正 
ERROR_CORRECT_H. 30%以下的错误会被纠正
boxsize: 每个点（方块）中的像素个数,默认10
border: 二维码距图像外围边框距离，默认为4，而且相关规定最小为4
'''