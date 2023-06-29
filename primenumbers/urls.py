from django.urls import path

from primenumbers.views import search

urlpatterns = [
    path('search/', search, name='search'),
]
