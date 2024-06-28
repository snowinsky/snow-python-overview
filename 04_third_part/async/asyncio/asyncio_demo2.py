import asyncio
import time
import requests


async def async_print(s):
    print(time.strftime("%H%M%S"), s)
# 定义一个协程函数，用async修饰过的函数不能直接调用，直接调用的话，只返回协程对象
async def time_sleep(sec):
    await async_print('start' + str(sec))
    try:
        requests.get("https://2qwerqwrwqer", verify=False)
    except:
        pass
    await async_print('end'+ str(sec))


async def run_time_sleep(sec):
    await time_sleep(sec)

async def some_task(sec1, sec2):
    task1 = time_sleep(sec1)
    task2 = time_sleep(sec2)
    asyncio.run(task1)
    asyncio.run(task2)

async def async_time_sleep(sec1, sec2):
    await run_time_sleep(sec1)
    await run_time_sleep(sec2)

if __name__ == '__main__':
    start = time.perf_counter()
    # task1 = asyncio.create_task(time_sleep(2))
    # asyncio.run(some_task(2,3))
    aa = time_sleep(3)
    # asyncio.run(aa)
    asyncio.run(async_time_sleep(2,3))
    end = time.perf_counter()
    print(f'cost={end-start}')
