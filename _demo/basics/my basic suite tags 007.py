import asyncio
from test_rest_api import test


@test()
async def basic_testcase_1():
    await asyncio.sleep(1)


@test()
async def basic_testcase_2():
    await asyncio.sleep(1)


@test()
async def basic_testcase_3():
    await asyncio.sleep(1)


@test()
async def basic_testcase_4():
    await asyncio.sleep(1)


@test()
async def basic_testcase_5():
    await asyncio.sleep(1)
