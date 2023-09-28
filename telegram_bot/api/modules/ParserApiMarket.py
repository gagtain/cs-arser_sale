from typing import List

from bs4 import BeautifulSoup

from api.schemas import Weapons
from api.schemas.Weapons import Weapon


class ParserApiMarket:

    def get_weapons_price(self, results_html):
        soup = BeautifulSoup(results_html, 'html.parser')
        listing_rows = soup.find_all('div', class_='market_listing_row')

        for row in listing_rows:
            price_tag = row.find('span', class_='market_listing_price_with_fee')

            if price_tag:
                price = price_tag.text.strip()
                yield price
            else:
                yield None

    async def get_weapons_list(self, results_html) -> List[Weapon]:
        weapons_list = []
        soup = BeautifulSoup(results_html, 'html.parser')
        listing_rows = soup.find_all('span', class_='market_listing_item_name')

        for row in listing_rows:
            weapon = Weapon()
            weapon.name = row.text.strip()
            weapon.price = self.get_weapons_price(results_html=results_html)
            weapons_list.append(weapon)
        return weapons_list
