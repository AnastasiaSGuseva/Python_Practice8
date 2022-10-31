def t_timetable_view(id):
    with open('t_timetable.txt', 'r', encoding='UTF-8') as f:
        rasp = f.read().split(', ')
        for i in range(len(rasp)):
            if id == rasp[i]:
                print(rasp[i+1])

def s_timetable_view(group):
    if group == '1':
        with open('s1_timetable.txt', 'r', encoding='UTF-8') as f:
            rasp = f.read()
            print(rasp)
    if group == '2':
        with open('s2_timetable.txt', 'r', encoding='UTF-8') as f:
            rasp = f.read()
            print(rasp)
    if group == '3':
        with open('s3_timetable.txt', 'r', encoding='UTF-8') as f:
            rasp = f.read()
            print(rasp)
