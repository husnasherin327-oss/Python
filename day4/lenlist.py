# row=int(input("enter the no of rows:"))
# for i in range(1,row+1):
#     print(' '*(row-i)+ " *"*i)
# for i in range(row-1,0,-1):
#      print(' '*(row-i)+ " *"*i)   
# row=int(input("enter the rows:"))

# for i in range(row):
#     for j in range(i):
#         print( " ",end=" ")
#     for j in range(row):
#         print( "*",end=" ")
#     print()
# row=int(input("enter the rows:")) 
# for i in range(row):
#    for j in range(row):
#       if j==0 or i==0 or i==row-1 or j==row-1:
#          print("*",end=" ")
#       else:
#          print(' ',end=" ")
        
      
#    print()
# def palindrome(string):
#     reverse_string=string[::-1]
#     if reverse_string==string:
#         return " its a palindrome"
#     else:
#         return "not a palindrome"
# print(palindrome("book"))
# def count_vowels(string):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in string:
#         if char in vowels:
#          count+=1
#     return count
# print(count_vowels("husna"))    
# num=[2,4,6,7,8]
# def max_in_list(num):
#     max_num=num[0]
#     for i in num:
#         if i> max_num:
#             max_num=i
#     return max_num
# print(max_in_list(num))
# num=[2,4,6,7,8]
# def min_in_list(num):
#     min_num=num[0]
#     for i in num:
#         if i< min_num:
#             min_num=i
#     return min_num
# print(min_in_list(num))  
# num=[2,4,6,7,8]
# def min_max_in_list(num):
#     min_num=num[0]
#     max_num=num[0]
#     for i in num:
#         if i< min_num:
#             min_num=i
        
#         if i>max_num:
#             max_num=i
#     return min_num, max_num

# print(min_max_in_list(num))
# l1=[2,4,5,6,7,8,9,24,1,3,11]
# l2=[3,1,4,9,7,8]

# merge=l1+l2
# merge.sort()
# new=list(set(merge))
#  print(new)
# for ch in range(1,101):
#     if ch%3==0 and ch%5==0:
#      print(ch)
# def chek_prime(a):
    
#     if a%1==0 and a%a==0:
#         return "true"
# print(chek_prime())    
# def mul_tab(a):
#     for i in range(1,11):
     
#      print(a, "x", i, "=", a * i)
# print(mul_tab(5))    
# row=int(input("enter the no of rows:"))
# for i in range(1,row+1):
   
#    for j in range (1,i+1):
#       print( ' ' *i+(row-i)*i)
# print() 
# l=[2,3,4,5,6,7,8]  
# def sum_even(l):
#     for i in l:
#         if
# li1=[2,3,4,5,6,7,8]
# print(max(li1))
# print(min(li1))
# list1=[2,4,1,9,5]
# new=sorted(list1)
# reve=new[::-1]
# print(reve)
row=int(input("row"))
for i in range(1,row+1):
    print("* "*i)