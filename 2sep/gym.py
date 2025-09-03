n=int(input())
price=0
if n>1 and n<6:
    price=500*n
elif n>=6 and n<12:
    rem=n-6
    price=2700+rem*500
else:
    rem=n-12
    price=5000+rem*500