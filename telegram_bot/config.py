import os


class Config:
    Minimum_total_price = 0.0
    Stickers_price = 0.0
    stickers_price_2 = 0.0
    stickers_price_3 = 0.0
    stickers_price_4 = 0.0


def init_config():
    Config.Minimum_total_price = float(os.environ.get("Minimum_total_price"))
    Config.Stickers_price = float(os.environ.get("Stickers_price"))
    Config.stickers_price_2 = float(os.environ.get("2_stickers_price"))
    Config.stickers_price_3 = float(os.environ.get("3_stickers_price"))
    Config.stickers_price_4 = float(os.environ.get("4_stickers_price"))
