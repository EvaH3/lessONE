N=7
A=[0]*N
max=0
buf=0

for i in range (N): A[i]=int(input())
for i in range(N-1):
    buf=abs(A[i+1]-A[i])
    if buf>max: max=buf

print(max*100)