a=int(input("Введите a: "))
b=int(input("Введите b: "))
c=int(input("Введите с. Если переменной нет, то введите 0: "))

def volume(a,b,c):
    if c==0: return int(a*b)
    else: return int(a*b*c)

V=volume(a,b,c)

print(V)