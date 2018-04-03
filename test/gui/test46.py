# 图形界面

'''
Python支持多种图形界面的第三方库，包括：
Tk
wxWidgets
Qt
GTK
等等。

但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行GUI编程。

Tkinter
我们来梳理一下概念：
我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；
Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
所以，我们的代码只需要调用Tkinter提供的接口就可以了。
'''


'''
# 第一个GUI程序
# 使用Tkinter十分简单，我们来编写一个GUI版本的“Hello, world!”。

# 第一步是导入Tkinter包的所有内容：
from tkinter import *

# 第二步是从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

# 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
# 在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。

# 第三步，实例化Application，并启动消息循环
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

# GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理。
'''


'''
# 输入文本
# 我们再对这个GUI程序改进一下，加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

# 当用户点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本后，使用tkMessageBox.showinfo()可以弹出消息对话框。
'''


# 练习 | BMI计算器
from tkinter import *
import tkinter.messagebox as messagebox
import re

# BMI指数（即身体质量指数，简称体质指数又称体重，英文为BodyMassIndex，简称BMI），是用体重公斤数除以身高米数平方得出的数字
def BMI(high,weigh):
    if not high or not weigh:
        return None

    reg = r'\d+(\.?\d+)?$'
    if not re.match(reg, high) or not re.match(reg, weigh):
        return ("参数输入有误，请输入数字。")

    high_pow = pow(float(high) / 100, 2)
    BMI = round((float(weigh)) / high_pow, 1)  # 保留小数点后一位小数

    msg = ''
    if BMI < 18.5 :
        msg = '偏瘦'
    elif BMI <= 25:
        msg = '正常'
    elif BMI <= 28:
        msg = '过重'
    elif BMI <= 32:
        msg = '肥胖'
    else:
        msg = '非常肥胖'
    return '您的BMI指数为%.1f，您的身体情况属于%s' % (BMI, msg)

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self, text='请输入您的身高(厘米):')
        self.label1.pack()
        self.nameInput1 = Entry(self)
        self.nameInput1.pack()
        self.label2 = Label(self, text='请输入您的体重(公斤):')
        self.label2.pack()
        self.nameInput2 = Entry(self)
        self.nameInput2.pack()
        self.alertButton = Button(self, text='点击显示结果', command=self.result)
        self.alertButton.pack()

    def result(self):
        BMI_result = BMI(self.nameInput1.get(), self.nameInput2.get()) or '请输入您的参数'
        messagebox.showinfo("BMI转换结果", '%s' % BMI_result)

app = Application()
app.master.title("BMI转换器")
app.mainloop()


# 小结
# Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。
