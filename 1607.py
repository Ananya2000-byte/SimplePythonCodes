I = input("Enter the string: ")
S = I.upper()
freq = {}
for i in I:
    if i != " ":
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
print(freq)
