import time
tm = time.localtime(time.time())
# print('year:', tm.tm_year)
# print('month:', tm.tm_mon)
# print('day:', tm.tm_mday)
# print('hour:', tm.tm_hour)
# print('minute:', tm.tm_min)
# print('second:', tm.tm_sec)
write = []
like_or_hate = []
time_list = []
while True:
    choice = input('(w)rite (r)ead (l)ike (h)ate: ')

    if choice == "w":
        sentence = input('write your thinking: ')
        write.append(sentence)
        like_or_hate.append([0, 0])
        print('hour:', tm.tm_hour)
        print('minute:', tm.tm_min)
        print('second:', tm.tm_sec)
        time_list.append([tm.tm_hour, tm.tm_min, tm.tm_sec])

    elif choice == "r":
        for i in range(len(write)):
            print("{} as line".format(i + 1))
            print(write[i])
            print('like {} and hate {}'.format(like_or_hate[i][0], like_or_hate[i][1]))
        print('hour:', tm.tm_hour)
        print('minute:', tm.tm_min)
        print('second:', tm.tm_sec)
    elif choice == "l":

        line_choice = int(input('Which line: '))
        like_or_hate[line_choice -1][0] += 1
        print('hour:', tm.tm_hour)
        print('minute:', tm.tm_min)
        print('second:', tm.tm_sec)
    elif choice == "h":
        line_choice = int(input('Which line:' ))
        like_or_hate[line_choice -1][1] += 1
        print('hour:', tm.tm_hour)
        print('minute:', tm.tm_min)
        print('second:', tm.tm_sec)