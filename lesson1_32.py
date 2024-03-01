threshold = float(input())

out=[]
i=0
point=0

with open('freqs.txt','rt', encoding='utf-8') as f:
    while True:
        char = f.read(1)
        if (char=='@'): break
        elif (char==';'):
            point=f.tell()
            print(point)
            f.seek(i)
            out.append(float(f.read(point-i-1)))
            f.seek(point)
            i=point

for n in range(len(out)):
    if (out[n]<=threshold):
        print(out[n], end='; ')