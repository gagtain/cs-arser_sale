from urllib import parse

from aiogram import Router, F, types

from api.modules.BaseApiMarket import BaseApiMarket
from api.schemas.Weapons import Weapon
from bot import a

router = Router()


@router.message(F.text.in_(['/start']))
async def echo_handler(message: types.Message) -> None:
    benefit_weapons_list = await a()
    for benefit_weapon in benefit_weapons_list:
        w: Weapon = benefit_weapon.weapon
        text = f"{w.name}\n\n" \
               f"Цена: {w.price} {w.currency}\n\n" \
               f"Стикеры\n" \
               f"ID {w.id_}\n" \
               f"Выгода {benefit_weapon.benefit} {benefit_weapon.currency}\n"
        for i in w.stickers:
            text += f"{i.name} {i.price} {i.currency}\n"

        url_ = parse.quote(w.name.encode('utf8'))
        text += f"{BaseApiMarket.api_url}{url_}#{w.id_}"
        await message.answer(text=text)
