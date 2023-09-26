from typing import List

from dataclasses_json import dataclass_json
from dataclasses import dataclass


class Sticker:
    name: str


class Weapon:
    """ Схема оружия, требует дальнейших изменений """
    name: str
    stickers: List[Sticker]
