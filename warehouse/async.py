import time
import asyncio

async def f1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('f1 end')

async def f2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('f2 end')

async def m():
    t1 = asyncio.create_task(f1(4))
    t2 = asyncio.create_task(f2(4))
    await t1
    await t2

print(time.strftime('%X'))

asyncio.run(m())

print(time.strftime('%X'))

def f3(x):
    print(x**2)
    time.sleep(3)
    print('end f3')
print(type(f3))
print(type(f3(4)))

