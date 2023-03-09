set_a={'col','mex','bol'}
set_b={'pe','col'}

set_c_1=set_a.union(set_b)
print(set_c_1)

set_c_1a=set_a | set_b
print(set_c_1a)

set_c_2 = set_a.intersection(set_b)
print(set_c_2)

set_c_2a = set_a & set_b
print(set_c_2a)

set_c_3 = set_a.difference(set_b)
print(set_c_3)

set_c_3a = set_a - set_b
print(set_c_3a)

set_c_4=set_a.symmetric_difference(set_b)
print(set_c_4)

set_c_4a=set_a ^ set_b
print(set_c_4a)