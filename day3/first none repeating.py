s=input("enter the string")
for ch in s:
    count=0
    for ch in s:
        if ch == ch:
            count=count+1
        else:
            break
