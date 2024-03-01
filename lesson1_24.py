import math

func=input()
a=int(input())
b=int(input())
N=int(input())
def trapez(func, a, b, N):
    i=a
    sum=0
    h=(b-a)/N
    funcorig = func
    func+="("
    func2 = func
    func+="0"
    func2+="0"
    func+=")"
    func2+=")"
    while i<=b:
        sum+=(eval(func.replace("0", str(i)))+eval(func2.replace("0", str(i + h))))
        i+=h
    sum=sum*h/2
    print(round(sum, 8))

trapez(func, a, b, N)
