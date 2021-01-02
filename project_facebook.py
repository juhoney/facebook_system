import time
tm = time.localtime(time.time())
# print('year:', tm.tm_year)
print('month:', tm.tm_mon)
print('day:', tm.tm_mday)
print('hour:', tm.tm_hour)
print('minute:', tm.tm_min)
print('second:', tm.tm_sec)

write = []
like_or_hate = []
time_list = []
login = []
def bubble_sort(time_list, like_or_hate):
    for i in range(len(time_list) - 1, 0, -1):
        for j in range(i):
            if time_list[j] > time_list[j + 1]:
                time_list[j], time_list[j + 1] = time_list[j + 1], time_list[j]
                like_or_hate[j], like_or_hate[j + 1] = like_or_hate[j + 1], like_or_hate[j]

while True:
    login_answer = input('Input login id: ')
    login.append(login_answer)
    choice = input('(w)rite (r)ead (l)ike (h)ate: ')
    tm = time.localtime(time.time())
    if choice == "w":
        sentence = input('write your thinking: ')
        write.append(sentence)
        like_or_hate.append([0, 0])
        print('month:', tm.tm_mon, 'day:', tm.tm_mday, 'hour:', tm.tm_hour, 'minute:', tm.tm_min, 'second:', tm.tm_sec)
        time_list.append(tm.tm_mon + tm.tm_mday + tm.tm_hour + tm.tm_min + tm.tm_sec)

    elif choice == "r":
        bubble_sort(time_list, like_or_hate)
        for i in range(len(write)):
            print("{} as line".format(i + 1))
            print(write[i])
            print('like {} and hate {}'.format(like_or_hate[i][0], like_or_hate[i][1]))
        print('month:', tm.tm_mon, 'day:', tm.tm_mday, 'hour:', tm.tm_hour, 'minute:', tm.tm_min, 'second:', tm.tm_sec)
        print(time_list)

    elif choice == "l":
        tm = time.localtime(time.time())
        line_choice = int(input('Which line: '))
        like_or_hate[line_choice -1][0] += 1
        print()
        print('month:', tm.tm_mon, 'day:', tm.tm_mday, 'hour:', tm.tm_hour, 'minute:', tm.tm_min, 'second:', tm.tm_sec)
        time_list[line_choice - 1] = tm.tm_mon + tm.tm_mday + tm.tm_hour + tm.tm_min + tm.tm_sec

    elif choice == "h":
        tm = time.localtime(time.time())
        line_choice = int(input('Which line:' ))
        like_or_hate[line_choice - 1][1] += 1
        print('month:', tm.tm_mon, 'day:', tm.tm_mday, 'hour:', tm.tm_hour, 'minute:', tm.tm_min, 'second:', tm.tm_sec)
        time_list[line_choice - 1] = tm.tm_mon + tm.tm_mday + tm.tm_hour + tm.tm_min + tm.tm_sec