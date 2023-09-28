from typing import List

import aiohttp
import requests
from fp.fp import FreeProxy



class BaseApiMarket:
    api_url = "https://steamcommunity.com/market/listings/730/"
    start = 0
    count = 100
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



    async def send(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=next(self.get_weapon_api()),

            ) as response:
                print(response.status, await response.text(), response.headers)
                if response.status != 200:
                    raise Exception
                return await response.json()

