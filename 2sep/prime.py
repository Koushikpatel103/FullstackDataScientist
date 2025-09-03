a=int(input())
n=a//2
count=0


for i in range(1,n+1):
    if a%2==0:
        count+=1
if count>1:
    print(" not Prime")
else:
    print(" prime")