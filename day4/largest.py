a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
if a>b and a>c:
    print("a is the largest",a)
elif b>c and b>a:
    print("b is the largest",b)
else:
    print("c is the largest",c)