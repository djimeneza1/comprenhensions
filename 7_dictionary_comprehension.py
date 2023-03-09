#{      key:value               for var in iterable     }
# elemento llave-valor          ciclos donde se extraen elementos de cualquier iterable

import random

'''
dict_1={}
for i in range(1,11):
    dict_1[i]=i*2

print(dict_1)

dict_1_v2={i:i*2 for i in range(1,11)}
'''

'''
countries=['col','mex','bol','pe']
population={}
for country in countries:
    population[country]=random.randint(100,999)
print(population)




population_v2={country:random.randint(100,999) for country in countries}
print(population_v2)
'''

names=['nico','zule','santi']
ages=[12,56,98]

print(zip(names,ages))

print(list(zip(names,ages)))

new_dict = {name:age for (name,age) in zip(names,ages)}

print(new_dict)
