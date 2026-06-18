import httpx

HTTP_TIME_OUT = 10  # 请求超时，秒


class AsHttpReq:
    """httpx 异步请求封装"""

    @staticmethod
    async def get(url, **kwargs):
        proxy = None
        async with httpx.AsyncClient(proxy=proxy) as client:
            response = await client.get(url, timeout=HTTP_TIME_OUT, **kwargs)
            return response

    @staticmethod
    async def post(url, **kwargs):
        proxy = None
        async with httpx.AsyncClient(proxy=proxy) as client:
            response = await client.post(url, timeout=HTTP_TIME_OUT, **kwargs)
            return response
