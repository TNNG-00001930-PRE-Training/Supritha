#7
l=[]
for i in range(1000, 3001):
    evendigit = True
    for digit in str(i):
        if int(digit) % 2 != 0:
            evendigit = False
            break
    if evendigit:
        l.append(str(i))

print(','.join(l))