n = int(input("Enter the number of items: "))

l = [int(input("Enter item: ")) for i in range(n)]

large, small = l[0], l[0]

for ele in l:
    if ele > large:
        large = ele
    if ele < small:
        small = ele

print("Largest:", large)
print("Smallest:", small)