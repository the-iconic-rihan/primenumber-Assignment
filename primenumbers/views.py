import csv
import json

from django.shortcuts import render

from primenumbers.models import Dish


def search(request):
    query = request.GET.get('query')
    dishes = []

    if query:
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if query.lower() in row['name'].lower():
                    items_dict = json.loads(row['items'])

                    full_details = json.loads(row['full_details'])

                    dish = Dish(name=row['name'], items=items_dict, full_details=json.dumps(full_details))
                    dishes.append(dish)

    return render(request, 'search.html', {'query': query, 'dishes': dishes})
