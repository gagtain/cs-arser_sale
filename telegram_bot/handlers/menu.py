

from aiogram import Router, F, types

from api.modules.BaseApiMarket import BaseApiMarket
from api.schemas.Weapons import Weapon
from bot import a

router = Router()


@router.message(F.text.in_(['/start']))
async def echo_handler(message: types.Message) -> None:
    weapons_list = await a()

    w: Weapon = weapons_list[1]
    text = f"{w.name}\n\n" \
           f"Цена: {w.price} {w.currency}\n\n" \
           f"Стикеры\n" \
           f"ID {w.id_}\n"
    for i in w.stickers:
        text += f"{i.name} {i.price} {i.currency}\n"

    url = f"{BaseApiMarket.api_url}{w.name}"
    url_ = url + f"#{w.id_}"
    text += url_.replace(' ', '%20').replace('/render', '')
    await message.answer(text=text)
