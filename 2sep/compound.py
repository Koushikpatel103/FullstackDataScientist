p=float(input("principal  "))
t=float(input("Time periood  " ))
r=float(input("rate  "))
ch=input("enter choice 1:si 2:ci ")
if ch == "si":
    si=(p*r*t)/100
    print("Simple intrest :",si)
    total=p+si
    print(total)
elif ch== "ci":
    ci=(p*((1+r/100)**t)-p)
    print("compound intresret :",ci)
    total=p+ci
    print(total)

else:
    print("invalid")

