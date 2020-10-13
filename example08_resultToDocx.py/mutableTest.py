a= [1, 2, 3, 4, 5]
b = a
print(id(a))
print(id(b))

b[0] = 0
print(a)