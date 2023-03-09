numbers=[1,2,3,4]

numbers_v2=[]
for i in numbers:
    numbers_v2.append(i*2)

numbers_v3=  list(map(lambda i:i*2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1=[1,2,3,4]
numbers_2=[6,7,8]

result=list(map( lambda x,y:x+y,numbers_1,numbers_2))
print(result)

items=[
    {
        'product':'camisas',
        'price':100
    },
    {
        'product':'pantalones',
        'price':200
    },
    {
        'product':'camisetas',
        'price':300
    },
]

prices=list(map(lambda item:item['price'],items))
print(items)
print(prices)

def add_taxes(item):
    item['taxes']=item['price']*0.18
    return item

new_items=list(map(add_taxes,items))
print(new_items)
print(items)



