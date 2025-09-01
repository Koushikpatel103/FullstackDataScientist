n=152
temp=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r*r*r
    n=n//10
if temp==sum:
    print("armstrong")
else:
    print("not a armstrong")

