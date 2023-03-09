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
    new_item=item.copy()
    new_item['taxes']=new_item['price']*0.18
    return new_item

new_items=list(map(add_taxes,items))
print('new list')
print(new_items)
print('old list')
print(items)



