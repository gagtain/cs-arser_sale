def add_weapon(name: str):
    with open('weapons.txt', encoding='utf-8', mode="w") as f:
        f.write(name + "\n")


def remove_weapon(name: str):
    with open('weapons.txt', encoding='utf-8', mode="w+") as f:
        text = f.read()
        text.replace(name, '')
        f.write(text + "\n")


def get_weapons():
    with open('weapons.txt', encoding='utf-8') as f:
        data = f.read().split('\n')
    return data


def get_proxy():
    with open('proxy.txt', encoding='utf-8') as f:
        data = f.read().split('\n')
    for proxy in data[0:-1]:
        yield proxy


class Proxy:
    def __init__(self):
        self.num = -1
        self.count_null = 0
        self.__set_proxy()
        self.end = len(self.proxy)

    def __set_proxy(self):
        with open('proxy.txt', encoding='utf-8') as f:
            data = f.read().split('\n')
        self.proxy = data[0:-1]

    def __iter__(self):
        return self.proxy[self.num]

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            try:
                return self.proxy[self.num]
            except:
                raise Exception

    def null_num(self):
        self.num = 0
        self.count_null += 1


proxy = Proxy()
