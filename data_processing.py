import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list

def aggregate(aggregation_key, aggregation_function, dict_list):
    out = []
    for item in dict_list:
        out.append(float(item[aggregation_key]))
    return aggregation_function(out)

_avg = lambda x: sum(x) / len(x)
_max = lambda x: max(x)
_min = lambda x: min(x)

scope_data1 = filter(lambda x: x['country'] == 'Italy', cities)
scope_data2 = filter(lambda x: x['country'] == 'Sweden', cities)

# - print the average temperature for all the cities in Italy
print("The average temperature for all the cities in Italy is: ")
print(aggregate("temperature", _avg, scope_data1))
print()
# - print the average temperature for all the cities in Sweden
print("The average temperature of all the cities in Sweden:")
print(aggregate("temperature", _avg, scope_data2))
print()
# - print the min temperature for all the cities in Italy
print("The average temperature of all the cities in Italy:")
print(aggregate("temperature", _min, scope_data1))
print()
# - print the max temperature for all the cities in Sweden
print("The average temperature of all the cities in Sweden:")
print(aggregate("temperature", _max, scope_data2))
print()