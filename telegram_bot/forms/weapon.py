from aiogram.fsm.state import StatesGroup, State


class WeaponForm(StatesGroup):
    name_add = State()
    name_remove = State()
