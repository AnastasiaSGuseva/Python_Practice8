import checker
import logger


def home_work_edit(id):
    with open('home_work.txt', 'r', encoding='UTF-8') as f:
        hw = f.read().split(', ')
        for i in range(len(hw)):
            if id == hw[i]:
                print('Ваш предмет: ', hw[i+1])
                logger.log('Просмотр домашнего задания по предмету', hw[i+1])
                print('Текущее домашнее задание: ', hw[i+2])
                print()
                print('Для редактирования домашнего задания введите 1')
                print('Для завершения просмотра домашнего задания введите 2')
                print()
                choice = input('Ваш выбор: ')
                choice = checker.check_to_2(choice)
                if choice == 1:
                    hw[i+2] = input('Введите новое домашнее задание: ')
                    with open('home_work.txt', 'w', encoding='UTF-8') as f:
                        f.write(', '.join(hw))
                    logger.log('Редактирование домашнего задания, новое задание: ', hw[i+2])
                    return
                else:
                    return


def home_work_view():
    subj = input('Введите название предмета: ').lower()
    logger.log('Ввод названия предмета', subj)

    with open('home_work.txt', 'r', encoding='UTF-8') as f:
        hw = f.read().split(', ')
        if subj in hw:
            for i in range(len(hw)):
                if subj == hw[i]:
                    print('Текущее домашнее задание: ', hw[i+1])
                    logger.log('Просмотр домашнего задания по предмету ', subj)
                    print()
                    print('Для просмотра домашнего задания по другому предмету введите 1')
                    print('Для завершения просмотра домашнего задания введите 2')
                    print()
                    choice = input('Ваш выбор: ')
                    choice = checker.check_to_2(choice)
                    if choice == 1:
                        home_work_view()
                    else:
                        return
        else:
            logger.log('Предмет не найден')
            print('Предмет не найден.\n')
            print('Чтобы выбрать другой предмет введите 1')
            print('Для завершения просмотра домашнего задания введите 2')
            print()
            choice1 = input('Ваш выбор: ')
            choice1 = checker.check_to_2(choice1)
            if choice1 == 1:
                home_work_view()
            else:
                return

