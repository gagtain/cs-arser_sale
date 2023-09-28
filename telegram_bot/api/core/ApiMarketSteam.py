import json
from pprint import pprint
from time import sleep

from api.modules.BaseApiMarket import BaseApiMarket
from api.modules.ParserApiMarket import ParserApiMarket


class ApiMarketSteam(BaseApiMarket):
    """ Высокоуровневый класс парсера """

    cookies = {

    }
    headers = {

    }

    parser = ParserApiMarket()

    async def parser_weapon(self, data=None):
        if data is None:
            data = await self.send()
        weapons_list = await self.parser.get_weapons_list(data=data)
        return weapons_list





