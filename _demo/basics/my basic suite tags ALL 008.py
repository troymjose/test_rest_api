import asyncio
from test_rest_api import test


@test(tags=['smoke', 'sanity'])
async def basic_testcase_1():
    await asyncio.sleep(1)


@test(tags=['smoke'])
async def basic_testcase_2():
    await asyncio.sleep(1)


@test(tags=['smoke'])
async def basic_testcase_3():
    await asyncio.sleep(1)


@test(tags=['ALL'])
async def login():
    await asyncio.sleep(1)


@test()
async def basic_testcase_5():
    await asyncio.sleep(1)
