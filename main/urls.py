from django.urls import path
from .views import *

urlpatterns = [
    path('foods/', foods),
    path('foods/categories/', food_category),
    path('foods/<category>', foods_by_category),
    path('destinations/', destinations),
    path('destinations/categories/', destination_category),
    path('destinations/<category>', destinations_by_category),
    path('restaurants/', restaurants),
    path('hotels/', hotels),
    path('hotels/categories/', hotel_category),
    path('hotels/<category>', hotels_by_category),
    path('comment/<address>/<int:id>/<user>/<int:rating>', comment),
    path('login/', login),
    path('register/', register),
]
