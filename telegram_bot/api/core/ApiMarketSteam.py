import json
from pprint import pprint
from time import sleep

from api.modules.BaseApiMarket import BaseApiMarket
from api.modules.BenefitWeapons import BenefitWeapons
from api.modules.ParserApiMarket import ParserApiMarket
from api.schemas.Weapons import BenefitWeapon


class ApiMarketSteam(BaseApiMarket):
    """ Высокоуровневый класс парсера """

    cookies = {

    }
    headers = {

    }

    parser = ParserApiMarket()

    async def parser_weapon(self, data=None) -> list[BenefitWeapon]:
        if data is None:
            data = await self.send()
        weapons_list = await self.parser.get_weapons_list(data=data)
        benefit_class = BenefitWeapons(weapons_list=weapons_list)
        benefit_weapons = benefit_class.get_benefit_weapons()
        return benefit_weapons





