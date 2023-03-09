import sys
print(sys.path)

import re
text='mi nombre es juan tengo 48 anhos mi numero de telefomno es 265-89654'
result=re.findall('[0-9]+',text)
print(result)


import time
timestamp=time.time()
print(timestamp)

local=time.localtime()
result=time.asctime(local)
print(result)

import collections
numbers=[1,2,32,45,2,1,1,1,3,54,6,7,7,8,2,4,6,7,0,98,1,2,3,4]
counter=collections.Counter(numbers)
print(counter)
