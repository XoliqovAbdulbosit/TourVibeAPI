from django.urls import path
from .views import *

urlpatterns = [
    path('foods/', foods),
    path('foods/categories/', food_category),
    path('foods/<category>', foods_by_category),
    path('destinations/', destinations),
    path('destinations/categories/', destination_category),
    path('destinations/states/', destination_state),
    path('destinations/<category>', destinations_by_category),
    path('destinations/state/<state>', destinations_by_state),
    path('restaurants/', restaurants),
    path('hotels/', hotels),
    path('hotels/categories/', hotel_category),
    path('hotels/<category>', hotels_by_category),
    path('comment/<address>/<int:id>/<user>/<rating>', comment),
    path('login/<email>/<password>', login),
    path('register/<email>/<password>/<name>/<country>', register),
    path('edit/<int:user_id>/<email>/<password>/<name>/<country>/<number>', edit),
]
