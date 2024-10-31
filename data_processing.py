import csv, os

class Travel:
    def __init__(self, dict_list=[]) -> None:
        self.dict_list = dict_list

    def filter(self, condition):
        filtered_list = []
        for item in self.dict_list:
            if condition(item):
                filtered_list.append(item)
        self.dict_list = filtered_list
    
    def aggregate(self, aggregation_key, aggregation_function):
        out = []
        for item in self.dict_list:
            out.append(float(item[aggregation_key]))
        return aggregation_function(out)

# get data
_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
_cities = []
with open(os.path.join(_location, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        _cities.append(dict(r))
_countries = []
with open(os.path.join(_location, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        _countries.append(dict(r))

# init class
italy = Travel(_cities)
sweden = Travel(_cities)
italy.filter(lambda x: x['country'] == 'Italy')
sweden.filter(lambda x: x['country'] == 'Sweden')

_avg = lambda x: sum(x) / len(x)
_max = lambda x: max(x)
_min = lambda x: min(x)

# - print the average temperature for all the cities in Italy
print("The average temperature for all the cities in Italy is: ")
print(italy.aggregate("temperature", _avg))
print()
# - print the average temperature for all the cities in Sweden
print("The average temperature of all the cities in Sweden:")
print(sweden.aggregate("temperature", _avg))
print()
# - print the min temperature for all the cities in Italy
print("The average temperature of all the cities in Italy:")
print(italy.aggregate("temperature", _min))
print()
# - print the max temperature for all the cities in Sweden
print("The average temperature of all the cities in Sweden:")
print(sweden.aggregate("temperature", _max))
print()