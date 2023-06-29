import json

from django.db import models

from json_encoder import CustomJSONEncoder


class Dish(models.Model):
    name = models.CharField(max_length=100)
    items = models.JSONField(encoder=CustomJSONEncoder)
    full_details = models.JSONField(encoder=CustomJSONEncoder)

    def __str__(self):
        return self.name

    def get_item_as_dict(self):
        return json.loads(self.items)

    def get_full_items_as_dict(self):
        return json.loads(self.full_details)
