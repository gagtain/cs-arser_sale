from urllib import parse

from aiogram import Router, F, types

from api.modules.BaseApiMarket import BaseApiMarket
from api.schemas.Weapons import Weapon
from config import Config
from start_benefit import get_benefit_weapons
from keyboards.main import main_keyboard
from services.excepted import TooManyRequests
from services.weapon import get_weapons

router = Router()


@router.message(F.text.in_(['/get_weapons']))
async def echo_handler(message: types.Message) -> None:
    if message.from_user.id == Config.user_id:
        try:
            weapon_data = get_weapons()
            if weapon_data[0] == '':
                await message.answer(text="Список ваших скинов пуст", reply_markup=main_keyboard)
            try:
                benefit_weapons_list_weapons = await get_benefit_weapons(weapon_data, many=True)
            except AttributeError as e:
                await message.answer(text=f"Сделайте запрос позже, api steam дало сбой.\n "
                                          f"Оригинальный код ошибки {str(e)}")
                return
            for benefit_weapons_list in benefit_weapons_list_weapons:
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
                    text += f"{BaseApiMarket.api_url}{url_}#{w.buy_url}"
                    await message.answer(text=text)
            await message.answer(text="Все", reply_markup=main_keyboard)
        except TooManyRequests:
            await message.answer(text="Не удалось отправить запрос из-за перегрузки запросами, проверьте прокси",
                                 reply_markup=main_keyboard)


@router.message(F.text.in_(['/start']))
async def echo_handler(message: types.Message) -> None:
    if message.from_user.id == Config.user_id:
        await message.answer(text="Ваш бот для поиска выгодных скинов", reply_markup=main_keyboard)