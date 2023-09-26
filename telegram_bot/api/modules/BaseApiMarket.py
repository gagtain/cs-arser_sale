from typing import List


class BaseApiMarket:
    api_url = "https://steamcommunity.com/market/listings/730/"
    start = 0
    count = 100
    country = "Ru"
    language = "english"
    cookies = {

    }
    headers = {

    }
    __weapon_data = None

    __weapon_url = None

    def __init__(self, weapon_data: str | List[str], many=False):
        if not many:
            self.__weapon_url = self.generate_api_url(weapon_data)
        else:
            self.__weapon_data = weapon_data
            self.__many = many

    def generate_api_url(self, weapon):
        return f"{self.api_url}{weapon}/render/?query=&start={self.start}" \
                              f"&count={self.count}&country={self.country}&language={self.language}"

    def get_weapon_api(self):
        if self.__many:
            for weapon in self.__weapon_data:
                yield self.generate_api_url(weapon=weapon)
        else:
            return self.__weapon_url

    async def send(self):
        ...
