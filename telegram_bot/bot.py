import asyncio

from api.core.ApiMarketSteam import ApiMarketSteam

api = ApiMarketSteam(weapon_data="AK-47%20%7C%20Fire%20Serpent%20(Field-Tested)")


asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.run(api.parser_weapon())
