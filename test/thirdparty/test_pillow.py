#　Pillow

# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
# 由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。

# 安装Pillow
# 如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：
# $ pip install pillow
# 如果遇到Permission denied安装失败，请加上sudo重试。


# 操作图像
# 来看看最常见的图像缩放操作，只需三四行代码

from PIL import Image

# 打开一个jpg图像文件
im = Image.open('../../files/images/test.jpg')
# 获得图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('../../files/images/thumbnail.jpg', 'jpeg')


# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
# 比如，模糊效果也只需几行代码：

from PIL import Image, ImageFilter

# 打开一个jpg图像文件
im = Image.open('../../files/images/test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('../../files/images/blur.jpg', 'jpeg')
print('模糊完毕...')


# 旋转
'''打开图像'''
catCopyIm = Image.open('../../files/images/test.jpg')
'''逆时针旋转90度的新Image图像'''
catCopyIm.rotate(90).save('../../files/images/rotate90.png')

'''逆时针旋转180度的新Image图像'''
catCopyIm.rotate(180).save('../../files/images/rotate180.png')

'''逆时针旋转270度的新Image图像'''
catCopyIm.rotate(270).save('../../files/images/rotate270.png')

# rotate()方法有一个可选的expand关键字参数，如果设为True，就会放大图像的尺寸，以适应整个旋转后的新图像
'''expand设置为True'''
catCopyIm.rotate(6, expand=True).save('../../files/images/roteat6_expand.png')

# transpose()方法，得到图像的”镜像翻转” 必须传入Image.FLIP_LEFT_RIGHT 或Image.FLIP_TOP_BOTTOM。
'''水平翻转'''
catCopyIm.transpose(Image.FLIP_LEFT_RIGHT).save('../../files/images/horizontal_flip.png')

'''垂直翻转'''
catCopyIm.transpose(Image.FLIP_TOP_BOTTOM).save('../../files/images/vertrical_flip.png')
print('旋转完毕...')



# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('../../files/fonts/arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('../../files/images/code.jpg', 'jpeg')
print('验证码图片生成完毕...')
