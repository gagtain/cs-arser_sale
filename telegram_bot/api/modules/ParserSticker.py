import re

import aiohttp
from bs4 import BeautifulSoup

from api.schemas.Weapons import Sticker
from a2 import get_sticker_data, get_sticker_data_json


class ParserSticker:
    api_url_base = "https://steamcommunity.com/market/listings/730/Sticker | "

    api_url = "https://steamcommunity.com/market/itemordershistogram?country=NL&language=russian&currency=5&two_factor=0"

    def get_api_url_base(self, sticker: Sticker):
        return f"{self.api_url_base}{sticker.name}"

    def get_api_url(self, id):
        return f"{self.api_url}&item_nameid={id}"

    async def send(self, url, text=True):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=url,

            ) as response:
                print(response.status, await response.text(), response.headers)
                if response.status != 200:
                    raise Exception
                if text:
                    return await response.text()
                else:
                    return await response.json()

    async def get_min_price(self, sticker: Sticker) -> float:
        url = self.get_api_url_base(sticker)
        data = get_sticker_data()
        id_sticker = self.get_id_sticker(data)
        url_to_id = self.get_api_url(id_sticker)
        data = get_sticker_data_json()
        text = data['sell_order_summary']
        regex = re.compile("<span class=\"market_commodity_orders_header_promote\">252</span><br>Начальная цена:"
                           " <span class=\"market_commodity_orders_header_promote\">(.*)<")
        min_price_sticker: str = regex.findall(text)
        return float(min_price_sticker[0][0: -5].replace(',', '.'))




    def get_id_sticker(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        price_tags = soup.find_all('div', class_='responsive_page_template_content')[0].find_all('script')[-1]
        regex = re.compile("Market_LoadOrderSpread(.*);")
        stickers_str: str = regex.findall(price_tags.text)
        return stickers_str[0].replace('(', '').replace(')', '').strip()