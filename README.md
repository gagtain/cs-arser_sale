# cs-arser_sale
### проект предназначенный для получения выгодных скинов из игры CS-GO в маркете steam
___
## Настройка

#### файл telegram_bot/.env
~~~
Minimum_total_price=100
Stickers_price=10
2_stickers_price=15
3_stickers_price=25
4_stickers_price=40
DEBUG=0
telegram_token=""
user_id=1
~~~
Minimum_total_price - минимальная прибыль со скина
Stickers_price - процент от цены стикера в случае если этот стикер 1\
2_stickers_price - процент от цены стикера в случае если этих стикеров 2\
3_stickers_price - процент от цены стикера в случае если этотих стикеров 3\
4_stickers_price - процент от цены стикера в случае если этих стикеров 4\
DEBUG - если 1, то режим отладки, если 2, то обычный режим работы\
telegram_token - токен телеграм бота\
user_id - идентификатор пользователя с которым должен работать бот\
count - количество просматриваемых лотов
___
#### файл telegram_bot/proxy.txt
~~~
http://xxxxx:xxxxxx@193.150.18x.24x:xxx
http://xxxxx:xxxxxx@193.150.1x8.8x:xxx
http://xxxxx:xxxxxx@84.32.2x.23x:xxx
http://xxxxx:xxxxxx@193.150.1x8.8x:xxx
http://xxxxx:xxxxxx@46.37.10x.10x:xxx
~~~
в данном файле через Enter необходимо указать proxy, как минимум 1.
## Дополнительно

Для меньшей загруженности, выбранные скины указываются в файле weapons.txt либо вручную, либо через бота

