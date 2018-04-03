# hello web


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


# 从environ里读取PATH_INFO，这样可以显示更加动态的内容
def application2(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    path = bytes(map(ord, environ['PATH_INFO'][1:])).decode('utf-8')
    body = '<h1>Hello, %s!</h1>' % (path or 'web')
    return [body.encode('utf-8')]