import datetime


def log(text='действие', value=None,):
    if value is None:
        value = ''
    date = datetime.datetime.now().strftime('%d-%m-%Y  %H:%M:%S')    

    with open('log.txt', 'a', encoding='UTF-8') as lg:
        lg.write(f'{date} {text} {value} \n')