import re

import aiohttp
from bs4 import BeautifulSoup
from api.schemas.Weapons import Sticker
from local_info import get_sticker_data_json
from config import Config, init_config
from services.excepted import TooManyRequests
from services.weapon import proxy


class ParserSticker:
    sticker_cache = {

    }
    api_url_base = "https://steamcommunity.com/market/listings/730/Sticker | "

    api_url = f"https://steamcommunity.com/market/itemordershistogram?country=NL&language=russian&count=100" \
              "&currency=5&two_factor=0"


    def get_api_url_base(self, sticker: Sticker):
        return f"{self.api_url_base}{sticker.name}"

    def clear_cache(self):
        self.sticker_cache = {

        }


    def get_api_url(self, id):
        return f"{self.api_url}&item_nameid={id}"

    async def send(self, url, text=True):
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
                    return await self.send(url=url, text=text)
                if text:
                    return await response.text()
                else:
                    return await response.json()

    async def get_min_price(self, sticker: Sticker) -> float:
        if not Config.DEBUG:
            data = await self.get_sticker_data_json(sticker, await self.get_data_sticker(sticker))
        else:
            data = get_sticker_data_json()
        text = data['sell_order_summary']
        regex = re.compile("<br>Начальная цена: <span class=\"market_commodity_orders_header_promote\">(.*)<")
        min_price_sticker: str = regex.findall(text)
        return float(min_price_sticker[0][0: -5].replace(',', '.'))

    async def get_data_sticker(self, sticker: Sticker):
        if self.sticker_cache.get(sticker.name):
            return self.sticker_cache.get(sticker.name)
        else:
            url = self.get_api_url_base(sticker)
            data = await self.send(url)
            self.sticker_cache[sticker.name] = data
            return data

    async def get_sticker_data_json(self, sticker, data) -> dict:
        if self.sticker_cache.get(f"{sticker.name}/json"):
            return self.sticker_cache.get(f"{sticker.name}/json")
        else:
            id_sticker = self.get_id_sticker(data)
            url_to_id = self.get_api_url(id_sticker)
            data = await self.send(url_to_id, text=False)
            self.sticker_cache[f"{sticker.name}/json"] = data
            return data



    def get_id_sticker(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        price_tags = soup.find_all('div', class_='responsive_page_template_content')[0].find_all('script')[-1]
        regex = re.compile("Market_LoadOrderSpread(.*);")
        stickers_str: str = regex.findall(price_tags.text)
        return stickers_str[0].replace('(', '').replace(')', '').strip()
