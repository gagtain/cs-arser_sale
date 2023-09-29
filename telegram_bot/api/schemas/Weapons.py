class Sticker:
    name = ""
    price = 0
    currency = "руб"

    def __repr__(self):
        return f"Название: {self.name}, Цена: {self.price}, Валюта цены: {self.currency}"

    def __str__(self):
        return f"Название: {self.name}, Цена: {self.price}, Валюта цены: {self.currency}"


class Weapon:
    name = ""
    price = 0
    currency = "руб"
    stickers = []
    id_ = ""

    buy_url = ""

    def __init__(self, name, price):
        self.name = name,
        self.price = price

    def __str__(self):
        return f"Название: {self.name}, Цена лота: {self.price}, Полная цена:{self.total}," \
               f" Валюта цены: {self.currency}, Стикеры: {self.stickers}"

    def __repr__(self):
        return f"Название: {self.name}, Цена лота: {self.price}, Полная цена:{self.total}," \
               f" Валюта цены: {self.currency}, Стикеры: {self.stickers}"

    def add_sticker(self, sticker: Sticker):
        self.stickers = [
            sticker, *self.stickers
        ]

    @property
    def total(self):
        total = 0.00
        for i in self.stickers:
            total += i.price

        return total + self.price


class BenefitWeapon:
    weapon: Weapon = None

    benefit: float = 0.0
    currency: str = "руб"


    def __init__(self, weapon, benefit):
        self.weapon = weapon
        self.benefit = benefit