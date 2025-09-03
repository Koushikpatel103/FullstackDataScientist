a=int(input())
b=int(input())
list=["1:add","2:sub","3:mul","div","modulos"]
print(list)
ch=int(input())
if(ch==1):
    res=a+b
    print(res)
elif(ch==2):
    res=a-b
    print(res)
elif(ch==3):
    res=a*b
    print(res)
elif(ch==4):
    res=a//b
    print(res)
elif(ch==5):
    res=a%b
    print(res)

else:
    print("input error")
