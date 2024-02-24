print("Задание №2")
#count_1 = int(input())
#count_2 = int(input())
#print(count_1+count_2)

print("Задание №3")
x=36/4*2
print(x)

print("Задание №4")
print(4*3**2*2)

print("Задание №5")
s="tomato"
t="cucumber"
print(2*s+t)

print("Задание №6")
s="change me"
print(s.replace("e","E",2))

print("Задание №7")
str_1 = "red"
str_2 = "white"
str_3 = "green"
print(str_1 + str_2)
print("_".join([str_1, str_2]))
print("_".join([str_1, str_2]))
print(str_3.find("a"))
print(str_2.find("e"))
print(str_3.find("r"))

print("Задание №8")
#N=10
#mass = [0]*N
#for i in range(N):
#    mass[i] = int(input())
#    i+=1
#print(mass[mass.index(max(mass))])

print("Задание №9")
x = [2, 4, 6, 8, 10, 12]
print(x[-1:2:-2])
print(x[::-2])
try:print(x[0::0])
except: print("Error")
print(x[1::3])
print(x[0])

print("Задание №10")
a=(2,"1",1,10,1)
print(a.index(1))

print("Задание №11")
melt = {'Sn':232, 'Zn':420, 'Fe':1539, 'Ni':1455, 'Si':1415, 'Be':1287}
#analog_1=input()
#analog_2=input()
#print(abs(melt.get(analog_1)-melt.get(analog_2)))

print("Задание №12")
s1 = ['Рентген', 'Лоренц', 'Зееман', 'Кюри', 'Милликен', 'Сигбан', 'Франк', 'Герц']
s2 = ['Фишер', 'Резерфорд', 'Кюри', 'Прегель']
i = 0
j = 0
for i in range (len(s1)):
    for j in range (len(s2)):
        if (s1[i]==s2[j]):
            print(s1[i])
        j+=1
    i+=1

print("Задание №13")
if 2**2>4:
    print("yes")

print("Задание №14")
if 10 >100:
    print("yes")
else:
    print("nope")

print("Задание №15")
a = 4
if a/2 >0:
    print('1')
elif a==4:
    print('2')
elif a < 0:
    print('3')
else:
    print('4')

print("Задание №16")
#x_0 = int(input())
#y_0 = int(input())
#circle = (x_0-1)**2+y_0**2
#if ((circle>=1 and circle<=2) or( x_0>=2 and x_0<=6 and y_0>=-5 and y_0<=1)):  print("yes yes")
#if (circle>=1 and circle<=2): print("yes no")
#if ( x_0>=2 and x_0<=6 and y_0>=-5 and y_0<=1): print("no yes")
#else: print("no no")

print("Задание №17")
#pol = input()
#char=pol[0]
#number=int(pol[1])
#if (number % 2 and (char=='b' or char=='d' or char=='f' or char=='h')): print("white")
#else: print("black")

print("Задание №18")
for i in range(3, 11, 4): print(i)

print("Задание №19")
lst = [2, 6, 43, 1, 66]
s = 0
for item in lst:
    if item % 2 == 0:
        s+=1
    else:
        continue

print("Задание №20")
n=0
part=1
x = float(input())
sum=0
while part>=0.000001:
    part=round(((-1)**(n))*(x**(n+1))/(n+1), 6)
    sum+=part
    n+=1
print(sum)
