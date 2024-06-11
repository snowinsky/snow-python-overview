import asyncio
import logging
import time


logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

async def task_sleep(sec_count):
    log.info(f'start task_sleep... at {time.time()}' )
    time.sleep(sec_count)
    log.info(f'end task_sleep... at {time.time()}')

async def async_task_sleep(sec_count):
    print("here1")
    await asyncio.sleep(sec_count)
    print("here2")


if __name__ == '__main__':
    # task_sleep(3)
    print("here11")
    asyncio.run(async_task_sleep(3))
    print("here22")
    time.sleep(4)
