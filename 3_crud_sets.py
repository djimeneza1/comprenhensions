set_countries={'col','mex','bol'}

size=len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add
set_countries.add('pe')
#print(set_countries.add('pe'))
print(set_countries)

#update
set_countries.update({'ar','ecua','pe'})
print(set_countries)

#remove
set_countries.remove('col')
print(set_countries)

#set_countries.remove('arg')
set_countries.discard('arg') #no usar remove por que da error, mejor discard
print(set_countries)

#clear
set_countries.clear()
print(set_countries)

