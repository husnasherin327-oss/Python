n = int(input("Enter the number of items: "))

l = [int(input("Enter item: ")) for i in range(n)]

unique_list = list(set(l))

unique_list.sort(reverse=True)  

if len(unique_list) >= 2:
    print("Second largest:", unique_list[1])
else:
    print("There is no second largest element")