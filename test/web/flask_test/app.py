# app

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '''<h1>Home</h1>
              <a href='/signin'>去登录</a>'''

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<h1>Login</h1>
              <form action="/signin" method="post">
              <p>username：<input name="username"/></p>
              <p>password：<input name="password" type="password"/></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 从request对象中读取表单数据
    if request.form['username'] == 'admin' and request.form['password'] == '123456':
        return '<h3>Hello, %s!</h3>' % request.form['username']
    return '<h3>用户名或密码输入错误</h3>'

if __name__ == '__main__':
    app.run()
