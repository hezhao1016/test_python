#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pip install threadpool

import threadpool
import time

def sayhello (a):
    print("hello: "+a)
    time.sleep(2)

def main():
    global result
    seed = ["a", "b", "c"]
    start = time.time()

    # 创建线程池
    task_pool = threadpool.ThreadPool(5)
    requests = threadpool.makeRequests(sayhello, seed)
    for req in requests:
        task_pool.putRequest(req)
    task_pool.wait()
    end = time.time()
    time_m = end-start
    print("线程池执行任务时间: "+str(time_m))

    start1 = time.time()
    for each in seed:
        sayhello(each)
    end1 = time.time()
    print("单线程执行任务时间: "+str(end1-start1))

if __name__ == '__main__':
    main()

# threadpool是一个比较老的模块了，现在虽然还有一些人在用，但已经不再是主流了
