#{      key:value               for var in iterable                                         if condition                    }
# elemento llave-valor          ciclos donde se extraen elementos de cualquier iterable     condicion para filtrar elementos

import random

countries=['col','mex','bol','pe']

population_v2={ country:random.randint(100,999) for country in countries }
print(population_v2)

result={ country:population for (country,population) in population_v2.items() if population>200 } 
print(result)

text='hola soy nicolas'
unique={c:c.upper() for c in text if c in 'aeiou'}
print(unique)