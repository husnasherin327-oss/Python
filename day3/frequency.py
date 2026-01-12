text=(input("enter the character:"))
freq={}
for ch in text:
    if ch in freq:          
        freq[ch] += 1
    else:                  
        freq[ch] = 1
print("character frequency dictnory")
print(freq)
