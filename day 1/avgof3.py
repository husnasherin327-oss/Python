# def average(a,b,c):
#     avg=(a+b+c)/3
#     return avg
# print(average(4,5,6))
# s1="husna" 
# s2="sherin"
# add=s1+s2
# print(add)
# dict1={
#     "anu":90,
#     "meenu":78,
#     "dilu":96,
# }
# topper=max(dict1,key=dict1.get)

# print(topper,dict1[topper])
# row = int(input("Enter the number of rows: "))
# for i in range(1, row + 1):
#     print()
#     for j in range(1,row+1):

#      print(''*(row-i),i*"*")
# print()
row = int(input("Enter the number of rows: "))
for i in range(row):
    for j in range(i):
        print( " ",end=" ")
    for j in range(row):
        print( "*",end=" ")
    print()