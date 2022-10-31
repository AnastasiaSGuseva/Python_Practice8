import checker
import student_menu
import teacher_menu
import logger


def main_menu():
    print('Выберите статус.')
    print('Введите 1, если вы преподаватель.')
    print('Введите 2, если вы студент.')
    print('Для выхода из программы введите 3')
    choice = input('Ваш выбор: ')
    choice = checker.check_to_3(choice)
    logger.log('Выбор статуса в главном меню', choice)
    print()
    if choice == 1:
        id = input('Введите id: ')
        logger.log('Ввод id', id)
        print()
        if checker.check_in_teachers(id) is True:
            teacher_menu.teacher_menu(id)
            print()
            main_menu()
        else:
            print('Вы ввели неверный id или статус. Попробуйте снова.')
            print()
            main_menu()
    if choice == 2:
        id = input('Введите id: ')
        logger.log('Ввод id', id)
        print()
        if checker.check_in_students(id) is True:
            group_numb = checker.check_in_group(id)
            logger.log('Группа студента', group_numb)
            student_menu.student_menu(id, group_numb)
            print()
            main_menu()
        else:
            print('Вы ввели неверный id или статус. Попробуйте снова.')
            print()
            main_menu()     
    if choice == 3:
        print('Всего доброго!\n')
        logger.log('Завершение работы')
        return


main_menu()