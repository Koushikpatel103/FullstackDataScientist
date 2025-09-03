a=int(input("Enter PIN:"))
pin=1234
balance=5000

if a==pin:
    print("Pin verfied ")
    w=int(input("enter amount to withdraw"))
    if w<balance:
        print("Withdrawal Succesfully Remaing balnce is ",balance-w)
    else:
        print("Insufficient balance")
else:
    print("incorect pin")