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

    async def parser_weapon(self):
        try:
            data = await self.send()
            weapons_list = await self.parser.get_weapons_list(results_html=data['results_html'])
            print(weapons_list)

        except Exception as e:
            print("Не удалось")
            sleep(60)
            await self.parser_weapon()




