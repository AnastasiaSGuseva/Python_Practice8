import checker
import home_work
import timetable
import logger


def student_menu(id, group):
    print('Выберите действие.')
    print('Для просмотра расписания введите 1')
    print('Для просмотра домашнего задания введите 2')
    print('Для выхода в главное меню нажмите 3.')
    s_choice = input('Ваш выбор: ')
    s_choice = checker.check_to_3(s_choice)
    logger.log('Выбор действия в меню студента', s_choice)
    print()
    if s_choice == 1:
        timetable.s_timetable_view(group)
        logger.log('Просмотр расписания для группы ', group)
        student_menu(id, group)
    if s_choice == 2:
        home_work.home_work_view()
        logger.log('Просмотр домашнего задания для группы', group)
        student_menu(id, group)
    if s_choice == 3:
        logger.log('Выход в главное меню')
        return
