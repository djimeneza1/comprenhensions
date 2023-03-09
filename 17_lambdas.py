def increment(x):
    return x+1

increment_lambda=lambda x:x+1

result=increment(10)
print(result)

result=increment_lambda(20)
print(result)


fullname = lambda name,lastname:f'Fullname is {name.title()} {lastname.title()}'

text=fullname('daniel','jimenez')
print(text)