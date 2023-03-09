def find_volume(lenght=1,width=1,depth=1):
    return lenght*width*depth, width, 'hola'

result=find_volume()
print(result)

result=find_volume(width=50)
print(result[0])

result, width, text = find_volume(width=50)
print(result)
print(width)
print(text)