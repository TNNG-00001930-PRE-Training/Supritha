#6
n=input()
n=n.split(" ")
n=sorted(n)
s=[]
for i in n:
    if i in s:
        continue
    else:
        s.append(i)
t=' '.join(s)
print(t)