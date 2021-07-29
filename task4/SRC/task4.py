
a = "кроме"
b = "старта"
c = False
d = "КО"
for i in b:
    if a == b or i == '*':
        c = True
    else:
        c = False

if c == False:
    d = "КО"
else:
    d = "ОК"

print(a + " " + b + " " + d)
    