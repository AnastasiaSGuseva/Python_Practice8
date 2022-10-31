import checker
import timetable
import home_work
import logger


def teacher_menu(id):
    print('Выберите действие.')
    print('Для просмотра расписания введите 1')
    print('Для просмотра и редактирования домашнего задания введите 2')
    print('Для выхода в главное меню нажмите 3.')
    t_choice = input('Ваш выбор: ')
    t_choice = checker.check_to_3(t_choice)
    logger.log('Выбор действия в меню преподавателя', t_choice)
    print()
    if t_choice == 1:
        timetable.t_timetable_view(id)
        logger.log('Просмотр расписания преподавателя, id', id)
        print()
        teacher_menu(id)
    if t_choice == 2:
        home_work.home_work_edit(id)
        print()
        teacher_menu(id)
    if t_choice == 3:
        logger.log('Выход в главное меню')
        return