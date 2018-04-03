# aiohttp

'''
asyncio可以实现单线程并发IO操作。

如果仅用在客户端，发挥的威力不大。
如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。

asyncio实现了TCP、UDP、SSL等协议
aiohttp则是基于asyncio实现的HTTP框架。
'''

# 先安装aiohttp：
# pip install aiohttp

# 然后编写一个HTTP服务器，分别处理以下URL：
# / - 首页返回b'<h1>Index</h1>'；
# /hello/{name} - 根据URL参数返回文本hello, %s!。


import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html', charset='utf-8')

async def hello(request):
    await asyncio.sleep(0.5)
    name = request.match_info.get('name') if request.match_info.get('name') else 'Default'
    text = '<h1>hello, %s!</h1>' % name
    return web.Response(body=text.encode('utf-8'), content_type='text/html', charset='utf-8')

# 注意aiohttp的初始化函数init()也是一个coroutine，loop.create_server()则利用asyncio创建TCP服务。
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello', hello)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


"""
web.Response(self, *, body=None, status=200,reason=None, text=None, headers=None, content_type=None, charset=None)
廖老师的不标记内容类型的话，默认是下载，可以加上content_type='text/html'

http://127.0.0.1/
<h1>Index</h1>

http://127.0.0.1/hello
404: Not Found

http://127.0.0.1/hello/TaoYuan
<h1>hello, TaoYuan!</h1>
"""
