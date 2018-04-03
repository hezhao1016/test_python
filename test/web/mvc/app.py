# mvc

from flask import Flask, request, session, render_template
import os

app = Flask(__name__)
# 使用session之前需要先设置SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('/login/form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == '123456':
        session['username'] = username  # 把用户名存到session中
        return render_template('/login/signin_ok.html', username=username)
    return render_template('/login/form.html', message='用户名或密码错误', username=username)

if __name__ == '__main__':
    app.run()
