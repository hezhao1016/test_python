import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}

#这里是非常关键的
session = requests.session()

def get_captcha():
    '''
    获取验证码图片
    :return:
    '''
    import time
    t = str(int(time.time()*1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    t = session.get(captcha_url, headers=headers)
    with open("captcha.jpg", "wb") as f:
        f.write(t.content)

    try:
        from PIL import Image
        im = Image.open("captcha.jpg")
        im.show()
        im.close()
    except:
        pass

    captcha = input("输入验证码>")
    return captcha


def zhihu_login(account, password):
    '''
    知乎登录
    :param account:
    :param password:
    :return:
    '''
    post_url = "https://www.zhihu.com/login/phone_num"
    captcha = get_captcha()

    post_data = {
        "phone_num":account,
        "password":password,
        'captcha':captcha,
    }
    response = session.post(post_url,data=post_data,headers=headers)
    res = json.loads(response.text)
    print(res)

# zhihu_login('131****2175','******')
