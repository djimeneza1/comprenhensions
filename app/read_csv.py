import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      '''
      paises = ["China", "India", "Estados Unidos", "Indonesia"]
      poblaciones = [1391, 1364, 327, 264]
      list(zip(paises, poblaciones))
      ----->>>>>>  [('China', 1391), ('India', 1364), ('Estados Unidos', 327), ('Indonesia', 264)]
      '''
      iterable = zip(header, row)   
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])