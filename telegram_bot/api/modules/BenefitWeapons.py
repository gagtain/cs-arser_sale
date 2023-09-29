import os

from config import Config
from api.schemas.Weapons import Weapon, BenefitWeapon, Sticker


class BenefitWeapons:
    __weapons_list: list[Weapon] = []

    __benefit_weapons_list: list[BenefitWeapon] = []

    def __init__(self, weapons_list):
        self.__weapons_list = weapons_list

    def get_benefit_weapons(self):
        for weapon in self.__weapons_list:
            benefit = self.get_benefit_weapon(weapon)
            if benefit > Config.Minimum_total_price:
                benefit_weapon = BenefitWeapon(weapon=weapon, benefit=benefit)
                self.__benefit_weapons_list.append(benefit_weapon)
        return self.__benefit_weapons_list

    def get_benefit_weapon(self, weapon: Weapon):
        return self.get_sum_stickers_price(weapon)

    def get_sum_stickers_price(self, weapon: Weapon):
        summ = 0.0
        for sticker in weapon.stickers:
            if sticker.price is not None:
                percent = self.get_percent_sticker(stickers=weapon.stickers, sticker=sticker)
                sticker_price_total = sticker.price * percent
                summ += round(sticker_price_total, 2)
        return summ

    def get_percent_sticker(self, stickers: list[Sticker], sticker: Sticker):

        count_sticker = len(list(filter(lambda x: x.name == sticker.name, stickers)))
        if count_sticker == 1:
            return Config.Stickers_price / 100
        if count_sticker == 2:
            return Config.stickers_price_2 / 100
        if count_sticker == 3:
            return Config.stickers_price_3 / 100
        if count_sticker == 4:
            return Config.stickers_price_4 / 100
