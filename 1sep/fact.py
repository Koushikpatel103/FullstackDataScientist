f=int(input())
if(f==0):
    print("1")
else:
    for i in range(f,1):
        f=f*i
        i=i-1

print(f)
