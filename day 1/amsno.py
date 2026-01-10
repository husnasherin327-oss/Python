def function(num):
    num_str=str(num)
    power= len(num_str)
    total=0
    for digit in num_str:
        total += int(digit) ** power
    
    return total == num
num=int(input("enter the number:"))
if function(num):
    print(num,"is an amstrong number")
else:
    print(num,"not an amstrong number")
