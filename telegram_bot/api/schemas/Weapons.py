class Sticker:
    name = 0
    price = 0


class Weapon:
    name = 0
    price = 0
    currency = ""
    stickers = list[Sticker]

    def __str__(self):
        return f"{self.name}, {self.price}, {self.currency}, {self.stickers}"
