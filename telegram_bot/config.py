import os


class Config:
    Minimum_total_price = 0.0
    Stickers_price = 0.0
    stickers_price_2 = 0.0
    stickers_price_3 = 0.0
    stickers_price_4 = 0.0
    count = 0
    user_id = ""
    telegram_token = ""
    DEBUG = False


def init_config():
    Config.Minimum_total_price = float(os.environ.get("Minimum_total_price"))
    Config.Stickers_price = float(os.environ.get("Stickers_price"))
    Config.stickers_price_2 = float(os.environ.get("2_stickers_price"))
    Config.stickers_price_3 = float(os.environ.get("3_stickers_price"))
    Config.stickers_price_4 = float(os.environ.get("4_stickers_price"))
    Config.user_id = int(os.environ.get("user_id"))
    Config.telegram_token = os.environ.get("telegram_token")
    Config.count = os.environ.get("count")
    deb = os.environ["DEBUG"]
    if deb == "1":
        Config.DEBUG = True
    else:
        Config.DEBUG = False
