import datetime


def welcome(name):
    time = int(datetime.datetime.now().strftime('%H'))
    if 6 < time < 12:
        print('Доброе утро, {}!'.format(name))
    if 12 < time < 18:
        print('Добрый день, {}!'.format(name))
    if 18 < time < 23:
        print('Добрый вечер, {}!'.format(name))
    if 0 < time < 6:
        print('Доброй ночи, {}!'.format(name))

