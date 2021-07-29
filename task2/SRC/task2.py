from math import sqrt


def funi(x, y, z, r, x1, y1, z1, x2, y2, z2):
    arr =[]
    rel = sqrt(x ** 2 + y ** 2 + z ** 2)
    relc = r + rel
    xi1 = x1
    xi2 = x2
    yi1 = y1
    yi2 = y2
    zi1 = z1
    zi2 = z2
    if x1 < x2:
        while xi1 < x2:
            if y1 < y2:
                while yi1 < y2:
                    if z1 < z2:
                        while zi1 < z2:
                            x3 = xi1 - x
                            y3 = yi1 - y
                            z3 = zi1 - z
                            rels = sqrt(x3 ** 2 + y3 ** 2 + z3 ** 2)
                            if rel < rels < relc:
                                arr.append("point: xi1, yi1, zi1")
                            zi1 += 0.1
                    elif z1 > z2:
                        while zi2 < z1:
                            x3 = xi2 - x
                            y3 = yi2 - y
                            z3 = zi2 - z
                            rels = sqrt(x3 ** 2 + y3 ** 2 + z3 ** 2)
                            if rel < rels < relc:
                                arr.append("point: xi1, yi1, zi2") 
                            zi2 += 0.1
                    yi1 += 0.1                         
            elif y1 > y2:
                while yi2 < y1:
                    if z1 < z2:
                        while zi1 < z2:
                            x3 = xi1 - x
                            y3 = yi1 - y
                            z3 = zi1 - z
                            rels = sqrt(x3 ** 2 + y3 ** 2 + z3 ** 2)
                            if rel < rels < relc:
                                arr.append("point: xi1, yi2, zi1")
                            zi1 += 0.1
                    elif z1 > z2:
                        while zi2 < z1:
                            x3 = xi2 - x
                            y3 = yi2 - y
                            z3 = zi2 - z
                            rels = sqrt(x3 ** 2 + y3 ** 2 + z3 ** 2)
                            if rel < rels < relc:
                                arr.append("point: xi1, yi2, zi2")
                            zi2 += 0.1
                    yi2 += 0.1
            xi1 += 0.1        
    elif x1 > x2:
        while xi2 < x1:
            if y1 < y2:
                while yi1 < y2:
                    if z1 < z2:
                        while zi1 < z2:
                            x3 = xi1 - x
                            y3 = yi1 - y
                            z3 = zi1 - z
                            rels = sqrt(x3 ** 2 + y3 ** 2 + z3 ** 2)
                            if rel < rels < relc:
                                arr.append("point: xi1, yi1, zi1")
                            zi1 += 0.1
                    elif z1 > z2:
                        while zi2 < z1:
                            x3 = xi2 - x
                            y3 = yi2 - y
                            z3 = zi2 - z
                            rels = sqrt(x3 ** 2 + y3 ** 2 + z3 ** 2)
                            if rel < rels < relc:
                                arr.append("point: xi2, yi1, zi2") 
                            zi2 += 0.1
                    yi1 += 0.1                         
            elif y1 > y2:
                while yi2 < y1:
                    if z1 < z2:
                        while zi1 < z2:
                            x3 = xi1 - x
                            y3 = yi1 - y
                            z3 = zi1 - z
                            rels = sqrt(x3 ** 2 + y3 ** 2 + z3 ** 2)
                            if rel < rels < relc:
                                arr.append("point: xi2, yi2, zi1")
                            zi1 += 0.1
                    elif z1 > z2:
                        while zi2 < z1:
                            x3 = xi2 - x
                            y3 = yi2 - y
                            z3 = zi2 - z
                            rels = sqrt(x3 ** 2 + y3 ** 2 + z3 ** 2)
                            if rel < rels < relc:
                                arr.append("point: xi2, yi2, zi2")
                            zi2 += 0.1
                    yi2 += 0.1
            xi2 += 0.1
            

    aplan = "точки столкновения сферы и прямой линии " + str(arr)
    bplan = "Коллизий не найдено"
    if len(arr) < 0:
        return aplan
    else:
        return bplan

class sphere: 
    center =  [0, 0, 0]
    radius = 10.67
    line =  [[1, 0.5, 15], [43, -14.6, 0.04]]
    c = center
    r = radius
    l = line

s = sphere

print(funi(s.c[0], s.c[1], s.c[2], s.r, s.l[0][0], s.l[0][1], s.l[0][2], s.l[1][0], s.l[1][1], s.l[1][2] ))    


    

