import math


def itobase(nb, base):
    ans = []
    i = base - 1
    while nb != 0:
        while i >= 0:
            if nb % base == i:
                ans.append(i)
                nb = nb // base
                break
            i -= 1
        i = base - 1
    ans.reverse()
    return ans


a = True  
while a == True:
    la = int(input("Ведите число: "))
    lb = int(input("Ведите систему исчесления от 2 до 9: "))
    if 1 < lb < 10:
        a = False
    else:
        print("Не  корректно введены данные")

print(itobase(la, lb))