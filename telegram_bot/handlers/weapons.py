from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from config import Config
from forms.weapon import WeaponForm
from services.weapon import add_weapon, remove_weapon, get_weapons

router = Router()


@router.message(F.text == 'Добавить оружие')
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    if message.from_user == Config.user_id:
        await state.set_state(WeaponForm.name_add)

        await message.answer(text="Напишите название скина")


@router.message(WeaponForm.name_add)
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    if message.from_user == Config.user_id:
        await state.clear()
        add_weapon(message.text)
        await message.answer(text="Скин добавлен")


@router.message(F.text == 'Убрать оружие')
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    if message.from_user == Config.user_id:
        await state.set_state(WeaponForm.name_remove)
        text = get_weapons()
        await message.answer(text="Варианты\n" + "\n".join(text))
        await message.answer(text="Напишите название скина")


@router.message(WeaponForm.name_remove)
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    if message.from_user == Config.user_id:
        await state.clear()
        remove_weapon(message.text)
        await message.answer(text="Скин убран")
