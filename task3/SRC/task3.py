from datetime import datetime



f = open(r"C:\Test\task3\SRC\log.txt", "w")
date_start = datetime.now()
barrel_volume = 200
water_volume = 32
bowl_volume = 20

bav = barrel_volume
wv = water_volume
bov = bowl_volume
attempt = 0 # количество попыток
fail = 0 # количество неудач
vp1 = 0 # сколько воды налито
vt1 = 0 # сколько воды было не налито, метод bow - wv
vp2 = 0 # сколько воды было забрано
vt2 = 0 # сколько воды было не забрано

tf = True
f.write("Program start " + str(date_start) + "\n")
f.write("META DATA :\n")
bav = int(input("Введите размер бочки "))
print("Размер бочки " + str(bav))
f.write("Размер бочки " + str(bav) + "\n")
wv = int(input("Введите обьем воды "))
start_wv = wv # обьем воды на начало периода
print("Обьем воды в бочке " + str(wv))
f.write("Обьем воды в бочке " + str(wv) + "\n")
print("Возможные команды +, - , stop")
while tf == True:
    qwest = input("ведите команду: ")
    if qwest == "stop" or qwest == "+" or qwest == "-":
        if qwest == "stop":
            print("программа завершена")
            date_finish = datetime.now()
            f.write("program finish " + str(date_finish) + "\n")
            f.write("Количетво попыток: " + str(attempt) + "\n")
            fail1 = fail / attempt * 100
            f.write("Процент ошибок: " + str(fail1)+ "\n")
            f.write("Объем воды был налит в бочку за указанный период: " + str(vp1) + "\n")
            f.write("Объем воды был не налит в бочку за указанный период: " + str(vt1) + "\n")
            f.write("Объем воды был взят из бочки за указанный период: " + str(vp2) + "\n")
            f.write("Объем воды был не взят из бочки за указанный период: " + str(vt2) + "\n")
            f.write("Объем воды в бочке в начале периода: " + str(start_wv) + "\n")
            f.write("Объем воды в бочке в конце периода: " + str(wv) + "\n")
            f.close()
            tf = False
            break
        bov = int(input("Количество воды которое хотите изменить "))
        wv_f = wv + bov
        wv_e = wv - bov
        if qwest == "+" and wv_f < bav and bav != wv:
            wv += bov
            attempt += 1
            vp1 += bov
            print("Обьем воды в бочке был увеличен на " + str(bov))
            print("Обьем воды в бочке " + str(wv))
            f.write("Обьем воды в бочке был увеличен на " + str(bov) + "\n")
            f.write("Обьем воды в бочке " + str(wv) + "\n")
        elif qwest == "-" and wv_e > 0 and wv != 0:
            attempt += 1
            wv -= bov
            vp2 += bov
            print("Обьем воды в бочке был уменьшен на " + str(bov))
            print("Обьем в бочке " + str(wv))
            f.write("Обьем воды в бочке был уменьшен на " + str(bov) + "\n")
            f.write("Обьем воды в бочке в бочке " + str(wv) + "\n")
        elif qwest == "+" and wv_f > bav and bav != wv:
            attempt += 1
            fail += 1
            h = bav - wv
            s_wv = wv
            s_bov = bov
            h1 = s_bov - (bav - s_wv)
            wv = bav
            vp1 += h
            vt1 += h1
            print("Обьем воды в бочке был увеличен на " + str(h))
            print("Обьем воды в бочке не был увеличен на " + str(h1))
            print("Обьем воды в бочке " + str(wv))
            f.write("Обьем воды в бочке был увеличен на " + str(h) + "\n")
            f.write("Обьем воды в бочке не был увеличен на " + str(h1) + "\n")
            f.write("Обьем воды в бочке " + str(wv) + "\n")
        elif qwest == "-" and wv_e < 0 and wv != 0:
            attempt += 1
            fail += 1
            s_wv = wv
            a = bov - wv
            wv = 0
            vp2 += s_wv
            vt2 += a
            print("Обьем воды в бочке был уменьшен на " + str(s_wv))
            print("Обьем воды в бочке не был уменьшен на " + str(a))
            print("Обьем воды в бочке " + str(wv))
            f.write("Обьем воды в бочке был уменьшен на " + str(s_wv) + "\n")
            f.write("Обьем воды в бочке не был уменьшен на " + str(a) + "\n")
            f.write("Обьем воды в бочке " + str(wv) + "\n")
        elif qwest == "+" and bav == wv:
            attempt += 1
            fail += 1
            vt1 += bov
            print("Обьем воды в бочке не может быть увеличен")
            print("Обьем в бочке " + str(wv))
        elif qwest == "-" and wv == 0:
            attempt += 1
            fail += 1
            vt2 += bov
            print("Обьем воды в бочке не может быть уменьшеньшен")
            print("Обьем в бочке " + str(wv))
    else:
        print("неправильная команда")

