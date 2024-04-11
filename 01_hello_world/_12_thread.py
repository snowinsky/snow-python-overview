#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import logging

logging.warning('This is a warning message')
logging.error("this is error mesage")
logging.info("this is info mesage")
logging.debug("this is debug mesage")

################## 最简单的线程的运用 #############

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)
        

# 创建线程
thread = threading.Thread(target=print_numbers)
thread1 = threading.Thread(target=print_numbers)

print(thread.getName(), thread.is_alive(), thread.isDaemon())

# 启动线程
thread.start()
thread1.start()

# 等待线程结束
thread.join()
thread1.join()

################## 最简单的线程的运用 #############

list1 = ['a','b']  # 可能在多个线程间共享的数据
for i in range(10):
    list1.append(i)

print(list1)

popLock = threading.Lock() # 控制共享数据的锁，锁和数据一定要在一个level上，或者说同一作用域中

# 消费共享数据的方法
def consumeList(threadName, list):
    popLock.acquire()
    elemet = list.pop()
    print(threadName, "consume the element=", elemet)
    popLock.release()

# 线程，消费共享数据的线程，可以定义多个参数，例如，给线程起名字，给线程传共享的数据  
class ConsumerThread(threading.Thread):
    def __init__(self, list, threadName):
        threading.Thread.__init__(self)
        self.list = list
        self.threadName = threadName
        
    def run(self):
        try:
            while True:
                if(len(self.list) == 0):
                    break
                else:
                    consumeList(self.threadName, self.list)
        except:
            pass
        
# 创建两个线程，同时消费一组共享数据，加锁和不加锁，效果不太一样
consumer1 = ConsumerThread(list1, "consumer1")
consumer2 = ConsumerThread(list1, "consumer2")

consumer1.start()
consumer2.start()

consumer1.join()
consumer2.join()

# 加锁的效果，同时只允许一个线程进入，所以，输出结果固定
# ['a', 'b', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# consumer1 consume the element= 9
# consumer1 consume the element= 8
# consumer1 consume the element= 7
# consumer1 consume the element= 6
# consumer1 consume the element= 5
# consumer1 consume the element= 4
# consumer1 consume the element= 3
# consumer1 consume the element= 2
# consumer1 consume the element= 1
# consumer1 consume the element= 0
# consumer1 consume the element= b
# consumer1 consume the element= a

# 不加锁的效果 多次执行，效果不固定
# consumer1 consume the element= 9
# consumer1 consume the element= 8
# consumer2 consume the element= 7
# consumer1 consume the element= 6
# consumer1 consume the element= 4
# consumer2 consume the element= 5
# consumer2 consume the element= 2
# consumer1 consume the element= 3
# consumer1 consume the element= 0
# consumer1 consume the element= b
# consumer2 consume the element= 1
# consumer1 consume the element= a

# consumer1 consume the element= 9
# consumer2 consume the element= 8
# consumer2 consume the element= 6
# consumer2 consume the element= 5
# consumer1 consume the element= 7
# consumer2 consume the element= 4
# consumer2 consume the element= 2
# consumer1 consume the element= 3
# consumer2 consume the element= 1
# consumer2 consume the element= b
# consumer2 consume the element= a
# consumer1 consume the element= 0
################## 最简单的线程的运用 #############

from concurrent.futures import ThreadPoolExecutor
import time


def spider(page):
    time.sleep(page)
    print(f"crawl task{page} finished")
    return page

with ThreadPoolExecutor(max_workers=5) as t:  # 创建一个最大容纳数量为5的线程池(with 语句就相当于try expect finally)
    task1 = t.submit(spider, 1)  # 第一个参数是方法名，第二个之后的参数是参数名，最好用paraName=paraValue的方式赋值，不容易出错
    task2 = t.submit(spider, 2)  # 通过submit提交执行的函数到线程池中
    task3 = t.submit(spider, 3)

    print(f"task1: {task1.done()}")  # 通过done来判断线程是否完成
    print(f"task2: {task2.done()}")
    print(f"task3: {task3.done()}")

    time.sleep(2.5)
    print(f"task1: {task1.done()}")
    print(f"task2: {task2.done()}")
    print(f"task3: {task3.done()}")
    print(task1.result())  # 通过result来获取返回值

################## 最简单的线程的运用 #############