import re
from typing import List

from bs4 import BeautifulSoup

from api.modules.ParserSticker import ParserSticker
from api.schemas.Weapons import Sticker
from api.schemas.Weapons import Weapon


class ParserApiMarket:
    parser_sticker = ParserSticker()

    def get_weapons_price(self, results_html):
        soup = BeautifulSoup(results_html, 'html.parser')
        price_tags = soup.find_all('span', class_='market_listing_price_with_fee')
        for price_tag in price_tags:

            if price_tag:
                price = price_tag.text.strip()
                yield price
            else:
                yield None

    async def get_weapons_list(self, data) -> List[Weapon]:
        weapons_list = []
        soup = BeautifulSoup(data['results_html'], 'html.parser')
        listing_rows = soup.find_all('span', class_='market_listing_item_name')
        price_iter = self.get_weapons_price(results_html=data['results_html'])
        for index, row in enumerate(listing_rows):
            price_result: str = next(price_iter)
            if price_result:
                weapon_price = price_result.replace('pуб.', ' ').strip().replace(',', '.')
            else:
                weapon_price = None
            weapon = Weapon(name=row.text, price=float(weapon_price))
            weapon.name = weapon.name[0]
            weapon.id_ = soup.find_all('div', class_="market_recent_listing_row")[index]['id']
            print(weapon.id_)
            await self.init_stickers(weapon=weapon, data=data, count=index)
            weapons_list.append(weapon)
        return weapons_list

    async def init_stickers(self, weapon: Weapon, data, count):
        list_weapons_assets: dict = data['assets']['730']['2']
        obj = list(list_weapons_assets.values())[count]
        stickers_list = obj['descriptions'][-1]['value']
        if 'Sticker:' in stickers_list:
            regex = re.compile("\<br>Sticker: (.*)\</center></div>")
            stickers_str: str = regex.findall(stickers_list)

            list_sticker_name = []
            if stickers_str:
                if '|' in stickers_str:
                    list_sticker_name = stickers_str[0].split(' | ')
                else:
                    list_sticker_name = stickers_str[0].split(', ')
            for sticker in list_sticker_name:
                sticker_class = Sticker()
                sticker_class.name = sticker
                price = await self.parser_sticker.get_min_price(sticker=sticker_class)
                sticker_class.price = price
                weapon.add_sticker(sticker_class)
