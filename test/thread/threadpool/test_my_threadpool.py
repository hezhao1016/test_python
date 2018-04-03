#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义线程池

# threadpool和concurrent.futures两种线程池的实现都是封装好的，任务只能在线程池初始化的时候添加一次，那么，假设我现在有这样一个需求，需要在线程池运行时，再往里面添加新的任务（注意，是新任务，不是新线程），那么要怎么办？
#
# 其实有两种方式：
#
# 1、重写threadpool或者future的函数：
#
# 这个方法需要阅读源模块的源码，必须搞清楚源模块线程池的实现机制才能正确的根据自己的需要重写其中的方法。
#
# 2、自己构建一个线程池：
#
# 这个方法就需要对线程池的有一个清晰的了解了，附上我自己构建的一个线程池：



from queue import Queue
import contextlib
import threading

# 代码来源： https://www.cnblogs.com/Eva-J/p/5106564.html

WorkerStop = object()

class ThreadPool:
    workers = 0

    threadFactory = threading.Thread
    currentThread = staticmethod(threading.currentThread)

    def __init__(self, maxthreads=20, name=None):
        self.q = Queue(0)
        self.max = maxthreads  # 线程池最大容量
        self.name = name
        self.waiters = []  # 空闲线程
        self.working = []  # 真实创建的线程列表

    def start(self):
        needSize = self.q.qsize()
        while self.workers < min(self.max, needSize):
            self.startAWorker()

    def startAWorker(self):
        self.workers += 1
        name = "PoolThread-%s-%s" % (self.name or id(self), self.workers)
        newThread = self.threadFactory(target=self._worker, name=name)
        newThread.start()

    def callInThread(self, func, *args, **kw):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param kw: 任务函数所需参数
        :return:
        """
        self.callInThreadWithCallback(None, func, *args, **kw)

    def callInThreadWithCallback(self, onResult, func, *args, **kw):
        """
        线程池执行一个任务(带回调函数)
        :param onResult: 回调函数
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param kw: 任务函数所需参数
        :return:
        """
        o = (func, args, kw, onResult)
        self.q.put(o)

    @contextlib.contextmanager
    def _workerState(self, stateList, workerThread):
        stateList.append(workerThread)
        try:
            yield
        finally:
            stateList.remove(workerThread)

    def _worker(self):
        ct = self.currentThread()
        o = self.q.get()
        while o is not WorkerStop:
            with self._workerState(self.working, ct):
                function, args, kwargs, onResult = o
                del o
                try:
                    result = function(*args, **kwargs)
                    success = True
                except:
                    success = False
                    if onResult is None:
                        pass

                    else:
                        pass

                del function, args, kwargs

                if onResult is not None:
                    try:
                        onResult(success, result)
                    except:
                        # context.call(ctx, log.err)
                        pass

                del onResult, result

            with self._workerState(self.waiters, ct):
                o = self.q.get()

    def stop(self):
        while self.workers:
            self.q.put(WorkerStop)
            self.workers -= 1


# 测试######################################
if __name__ == '__main__':
    def show(arg):
        import time
        time.sleep(1)
        print('执行任务: ', arg)

    pool = ThreadPool(20)

    for i in range(500):
        pool.callInThread(show, i)

    pool.callInThread(show, 'End')

    pool.start()
    pool.stop()
