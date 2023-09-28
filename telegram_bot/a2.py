import json


def get_sticker_data():
    with open('2.txt', encoding='utf-8') as e:
        return e.read()

def get_sticker_data_json():
    with open('3.txt', encoding='utf-8') as e:
        return json.load(e)