from typing import List

import aiohttp

from config import Config
from services.excepted import TooManyRequests
from services.weapon import proxy


class BaseApiMarket:
    api_url = "https://steamcommunity.com/market/listings/730/"
    start = 0
    count = 0
    country = "Ru"
    language = "english"
    currency = 5
    cookies = {

    }
    headers = {

    }
    weapon_data = None

    weapon_url = None

    def __init__(self, weapon_data: str | List[str], many=False):
        self.count = Config.count
        if not many:
            self.weapon_url = self.generate_api_url(weapon_data)
        else:
            self.weapon_data = weapon_data
        self.many = many

    def generate_api_url(self, weapon):
        return f"{self.api_url}{weapon}/render/?query=&start={self.start}" \
               f"&count={self.count}&country={self.country}" \
               f"&language={self.language}&currency={self.currency}"

    def get_weapon_api(self):
        if self.many:
            for weapon in self.weapon_data:
                yield self.generate_api_url(weapon=weapon)
        else:
            yield self.weapon_url

    async def send(self, url):
        async with aiohttp.ClientSession() as session:
            try:
                proxy_str = next(proxy)
            except StopIteration:
                proxy.null_num()
                proxy_str = next(proxy)
            except Exception:
                if proxy.count_null < 5:
                    proxy.null_num()
                    proxy_str = next(proxy)
                else:
                    raise TooManyRequests()
            async with session.post(
                    url=url,
                    proxy=proxy_str
            ) as response:
                if response.status != 200:
                    return await self.send(url=url)
                return await response.json()
