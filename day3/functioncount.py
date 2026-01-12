# def count():
#     count=[0]
#     for ch in list:
#         if max:
#             print("largest")
#         else:
#             print("smallest")
#     return
# print(count)
# row=int(input("enter the number"))
# for i in range(1,row+1):
#     print(' '*(row-i)+" *"*i)
# for i in range(row-1,0,-1):
#     print(' '*(row-i)+" *"*i)


#row=int(input("enter the no of rows:"))
# for i in range(1,row+1):
#     print(' '*(row-i)+ " *"*i)
# for i in range(row-1,0,-1):
#      print(' '*(row-i)+ " *"*i)
# row=int(input("enter the no of rows:"))  
# for i in range(row):
#     for j in range(i):
#         print( " ",end=" ")
#     for j in range(row):
#         print( "*",end=" ")
#     print()
# for i in range(row):
#     for j in range(i):
#         print( " ",end=" ")
#     for j in range(row):
#         print( "*",end=" ")
#     print()    
num=5
for i in range(1, num+1):
    for j in range(num-i):
        print('',end="")
    for j in range(i):
        print("*",end=" ")    
    print()        