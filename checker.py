import welcome


def check_in_group(id):
    with open('students1.txt', 'r', encoding='UTF-8') as f1:
        sp1 = f1.read()

    with open('students2.txt', 'r', encoding='UTF-8') as f2:
        sp2 = f2.read()

    with open('students3.txt', 'r', encoding='UTF-8') as f3:
        sp3 = f3.read()
        
    sp_itog = (sp1 + ', ' + sp2 + ', ' + sp3).split(', ')

    for i in range(len(sp_itog)):
        if id == sp_itog[i]:
            group = sp_itog[i+1]
    return group


def check_in_students(id):
    with open('students1.txt', 'r', encoding='UTF-8') as f1:
        sp1 = f1.read()

    with open('students2.txt', 'r', encoding='UTF-8') as f2:
        sp2 = f2.read()

    with open('students3.txt', 'r', encoding='UTF-8') as f3:
        sp3 = f3.read()
        
    sp_itog = (sp1 + ', ' + sp2 + ', ' + sp3).split(', ')

    flag = False
    for i in range(len(sp_itog)):
        if id == sp_itog[i]:
            flag = True
            name = sp_itog[i+2]

    if flag == True:
        welcome.welcome(name)
        print()
        return True
    else:
        return False


def check_in_teachers(id):
    with open('teachers.txt', 'r', encoding='UTF-8') as file:
        str_t = file.read().split(', ')

    flag = False
    for i in range(len(str_t)):
        if id == str_t[i]:
            flag = True
            name = str_t[i+1]

    if flag == True:
        welcome.welcome(name)
        print()
        return True
    else:
        return False


def check_to_4(ch):
    while not ch.isdigit():
        ch = input('Введите число: ')
    else:
        while int(ch) < 1 or int(ch) > 4:
            ch = input('Введите целое число от 1 до 4: ')
        else:
            return int(ch)


def check_to_3(ch):
    while not ch.isdigit():
        ch = input('Введите число: ')
    else:
        while int(ch) < 1 or int(ch) > 3:
            ch = input('Введите целое число от 1 до 3: ')
        else:
            return int(ch)


def check_to_2(ch):
    while not ch.isdigit():
        ch = input('Введите число: ')
    else:
        while int(ch) < 1 or int(ch) > 2:
            ch = input('Введите целое число от 1 до 2: ')
        else:
            return int(ch)
