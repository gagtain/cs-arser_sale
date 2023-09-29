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

    async def parser_weapon(self) -> list[list[BenefitWeapon]]:
        list_weapons = []
        list_sending = [[await self.send(url), url] for url in self.get_weapon_api()]
        for data in list_sending:
            print(data[1])
            weapons_list = await self.parser.get_weapons_list(data=data[0])
            benefit_class = BenefitWeapons(weapons_list=weapons_list)
            benefit_weapons = benefit_class.get_benefit_weapons()
            list_weapons.append(benefit_weapons)
        return list_weapons





