import csv

from primenumbers.models import Dish

with open('../data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    print(reader)

    for row in reader:
        name = row[0]
        items = row[1]
        full_details = row[2]
        dish = Dish(name=name, items=items, full_details=full_details)
        dish.save()
