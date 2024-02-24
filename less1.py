room = int(input())
limmit = 8
i = 0
podezd = 1

while True:
    for i in range (limmit-7,limmit):
        i+=1
    if room>i:
        limmit+=8
        podezd+=1
    else:
        break

print(8+(room-podezd*8), podezd)