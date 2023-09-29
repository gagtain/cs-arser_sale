import json


def get_sticker_data_json():
    with open('test/test3.txt', encoding='utf-8') as e:
        return json.load(e)
