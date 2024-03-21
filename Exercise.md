
1. Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
2. Use list comprehension to construct a new list but add 6 to each item.
3. Using list comprehension, construct a list from the squares of each element in the list.
4. Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
5. Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.

```python 
#5. Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
lst=[i.upper() for i in dict_ if dict_[i]<500]
print(lst)
#Type your answer here.

#lst=[]
#1.Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
a=[x for x in range(1200,2000,130)]
print(a)

#2. Use list comprehension to construct a new list but add 6 to each item.
b=[x+6 for x in a]
print(b)

#3. Using list comprehension, construct a list from the squares of each element in the list.
c=[x**2 for x in b]
print(c)

#4. Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
d=[x**2 for x in range(10) if (x**2>50)]
print(d)
#print(lst)

```