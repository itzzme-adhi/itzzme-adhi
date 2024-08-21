x=int(input("plese enter which option you want"))
if x==1:
    R=int(input("enter the radius of circle"))
    pi=3.14
    circum=2*pi*R
    print(circum)
elif x==2:
    R=int(input("enter the radius of circle"))
    pi=3.14
    area=pi*R**2
    print(area)
elif x==3:
    L=int(input("enter the length "))
    B=int(input("enter the breadth "))
    area=L*B
    print(area)
else:
    print("invalid options")