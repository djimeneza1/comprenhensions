# [element                   for element in iterable                                    if condition                 ]
#  elemento     ciclo donde se extraen elementos de cualquier iterable      condicion opcional para filtrar elementos 

#version normal
numbers=[]
for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i*2)
print(numbers)

numbers_v2 = [i*2 for i in range(1,11) if i%2==0]
print(numbers_v2)
