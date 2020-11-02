num=int(input("enter the number"))
if num % 2==0:
    if num % 3==0:
        print("divisual by 3 and 2")
    else:
        print(" disual by 2 not divisual by 3")
else:
    if num % 3==0:
        print("divisual by 3 not divisual by 2")
    else:
        print("not divisual by 2 not divisual by 3")
        