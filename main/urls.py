from django.urls import path
from .views import *

urlpatterns = [
    path('foods/', foods),
    path('foods/categories/', food_category),
    path('foods/<category>', foods_by_category),
    path('food/<int:id>', food_by_id),
    path('destinations/', destinations),
    path('destinations/categories/', destination_category),
    path('destinations/states/', destination_state),
    path('destinations/<category>', destinations_by_category),
    path('destinations/state/<state>', destinations_by_state),
    path('destination/<int:id>', destination_by_id),
    path('restaurants/', restaurants),
    path('restaurant/<int:id>', restaurant_by_id),
    path('hotels/', hotels),
    path('hotels/categories/', hotel_category),
    path('hotels/<category>', hotels_by_category),
    path('hotel/<int:id>', hotel_by_id),
    path('comment/<address>/<int:id>/<user>/<rating>', comment),
    path('login/<email>/<password>', login),
    path('register/<email>/<password>/<name>/<country>', register),
    path('edit/<int:user_id>/<email>/<password>/<name>/<country>/<number>', edit),
]
