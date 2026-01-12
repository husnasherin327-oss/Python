unit=float(input("enter the unit:"))
if unit>=100:
    print("15 rupees")
    if unit>=500:
        print("60 rupees")
    elif  unit>=1000:
        print("200 rupees")      
else:
    print("10 rupees")        