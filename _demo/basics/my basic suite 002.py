import asyncio
from test_rest_api import test


@test()
async def basic_testcase():
    await asyncio.sleep(1)
