from api.core.ApiMarketSteam import ApiMarketSteam
from api.schemas.Weapons import BenefitWeapon


async def get_benefit_weapons(weapon_data, many=False) -> list[list[BenefitWeapon]]:
    api = ApiMarketSteam(weapon_data=weapon_data[0:-1], many=many)
    print("Старт")
    return await api.parser_weapon()
