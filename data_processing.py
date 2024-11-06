import csv, os

class TableDB:
    def __init__(self):
        self.table_database = []
        self.__location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.__cities = []
        with open(os.path.join(self.__location, 'Cities.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.__cities.append(dict(r))
        self.__countries = []
        with open(os.path.join(self.__location, 'Countries.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.__countries.append(dict(r))

    @property
    def location(self):
        return self.__location

    @property
    def cities(self):
        return self.__cities

    @property
    def countries(self):
        return self.__countries

    def insert(self, table):
        if self.search(table) is None:
            self.table_database.append(table)

    def search(self, table_name):
        for tab in self.table_database:
            if tab == table_name:
                return tab
        return None

class Table:
    def __init__(self, table_name, table):
        self.__table = table
        self.__table_name = table_name

    @property
    def table(self):
        return self.__table
    
    @table.setter
    def table(self, lst):
        self.__table = lst

    @property
    def table_name(self):
        return self.__table_name
    
    @table_name.setter
    def table_name(self, name):
        self.__table_name = name

    def filter(self, condition):
        filtered_list = []
        for item in self.__table:
            if condition(item):
                filtered_list.append(item)
        self.__table = filtered_list
    
    def aggregate(self, aggregation_key, aggregation_function):
        out = []
        for item in self.__table:
            out.append(float(item[aggregation_key]))
        return aggregation_function(out)

    def __str__(self):
        out = ""
        for item in self.__table:
            for key, value in item.items():
                    out += f"{key} {value}"
            out += "\n"
        return out

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
tab1 = []
with open(os.path.join(location, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        tab1.append(dict(r))
tab2 = []
with open(os.path.join(location, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        tab2.append(dict(r))

# init class
tabdb = TableDB()
tabdb.insert(tab1)
tabdb.insert(tab2)

italy = Table('Italy', tabdb.cities)
italy.filter(lambda x: x["country"] == "Italy")

sweden = Table('Sweden', tabdb.cities)
sweden.filter(lambda x: x["country"] == "Sweden")

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
