#8
st=input()
st=list(st)
upper_case=0
lower_case=0
for i in range(len(st)):
    if ord(st[i])>=97 and ord(st[i])<=122:
        lower_case+=1
    elif ord(st[i])>=65 and ord(st[i])<=90:
        upper_case+=1
print('upper case',upper_case)
print('lower case',lower_case)