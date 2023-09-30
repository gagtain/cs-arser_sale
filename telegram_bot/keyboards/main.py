from aiogram import types

main_keyboard = types.ReplyKeyboardMarkup(keyboard=[[
    types.KeyboardButton(text="Добавить оружие"),
    types.KeyboardButton(text="Убрать оружие"),
    types.KeyboardButton(text="/get_weapons"),
    types.KeyboardButton(text="Очистить кэш")
]])
