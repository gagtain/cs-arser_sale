from api.core.ApiMarketSteam import ApiMarketSteam


def clear_cache_sticker():
    ApiMarketSteam.parser.parser_sticker.clear_cache()
