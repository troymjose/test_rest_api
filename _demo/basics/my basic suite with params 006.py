import asyncio
from test_rest_api import test


@test(name='My testcase name T001', desc="Description of my testcase", enabled=True, tags=(), is_async=True,
      execution_order='A0001')
async def basic_testcase():
    await asyncio.sleep(1)
