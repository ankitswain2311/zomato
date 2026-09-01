pin=1234
balance=10000
withdraw=9000
if pin==1234:
    if balance>=withdraw:
        print("withdraw successful")
    else:
        print("insufficient balance")
else:
    print("invalid pin")