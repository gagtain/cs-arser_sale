import asyncio
import json

from api.core.ApiMarketSteam import ApiMarketSteam
from api.schemas.Weapons import BenefitWeapon


async def a() -> list[BenefitWeapon]:
    api = ApiMarketSteam(weapon_data="AK-47%20%7C%20Fire%20Serpent%20(Field-Tested)")
    with open('1.txt', encoding='utf-8') as e:
        data = json.load(e)
    return await api.parser_weapon(data)
