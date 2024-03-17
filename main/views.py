from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def food_category(request):
    categories = set()
    for food in Food.objects.all():
        categories.update(food.category.split())
    return JsonResponse(list(categories), safe=False)


def foods(request):
    foods = [
        {
            'id': food.pk,
            'mainImage': food.mainImage,
            'images': [image.image for image in food.images.all()],
            'name': food.name,
            'description': food.description,
            'rating': food.rating,
            'comments': [{
                'id': comment.id,
                'author': {
                    'name': comment.author.name,
                    'email': comment.author.email,
                    'country': comment.author.country,
                    'image': comment.author.image,
                },
                'date': comment.date.strftime("%d/%m/%Y %H:%M:%S"),
                'rating': comment.rating,
                'text': comment.text,
            } for comment in food.comments.all()],
            'category': food.category.split(),
            'locatedCountry': food.locatedCountry,
            'locatedState': food.locatedState,
            'restaurant': [{
                'name': restaurant.name,
                'price': restaurant.price,
                'caloryInfo': restaurant.caloryInfo,
                'rating': restaurant.rating,
                'overViewVideo': restaurant.overViewVideo,
            } for restaurant in food.restaurant.all()],
        }
        for food in Food.objects.all()
    ]
    return JsonResponse(foods, safe=False)


def foods_by_category(request, category):
    foods = [
        {
            'id': food.pk,
            'mainImage': food.mainImage,
            'images': [image.image for image in food.images.all()],
            'name': food.name,
            'description': food.description,
            'rating': food.rating,
            'comments': [{
                'id': comment.id,
                'author': {
                    'name': comment.author.name,
                    'email': comment.author.email,
                    'country': comment.author.country,
                    'image': comment.author.image,
                },
                'date': comment.date.strftime("%d/%m/%Y %H:%M:%S"),
                'rating': comment.rating,
                'text': comment.text,
            } for comment in food.comments.all()],
            'category': food.category.split(),
            'locatedCountry': food.locatedCountry,
            'locatedState': food.locatedState,
            'restaurant': [{
                'name': restaurant.name,
                'price': restaurant.price,
                'caloryInfo': restaurant.caloryInfo,
                'rating': restaurant.rating,
                'overViewVideo': restaurant.overViewVideo,
            } for restaurant in food.restaurant.all()],
        }
        for food in Food.objects.filter(category__contains=category)
    ]
    return JsonResponse(foods, safe=False)


def hotels(request):
    hotels = [
        {
            'id': hotel.pk,
            'mainImage': hotel.mainImage,
            'name': hotel.name,
            'images': [image.image for image in hotel.images.all()],
            'description': hotel.description,
            'rating': hotel.rating,
            'comments': [{
                'id': comment.id,
                'author': {
                    'name': comment.author.name,
                    'email': comment.author.email,
                    'country': comment.author.country,
                    'image': comment.author.image,
                },
                'date': comment.date.strftime("%d/%m/%Y %H:%M:%S"),
                'rating': comment.rating,
                'text': comment.text,
            } for comment in hotel.comments.all()],
            'locatedCountry': hotel.locatedCountry,
            'locatedState': hotel.locatedState,
        }
        for hotel in Hotel.objects.all()
    ]
    return JsonResponse(hotels, safe=False)


def hotel_category(request):
    categories = set()
    for hotel in Hotel.objects.all():
        categories.add(hotel.locatedCountry)
    return JsonResponse(list(categories), safe=False)


def hotels_by_category(request, category):
    hotels = [
        {
            'id': hotel.pk,
            'mainImage': hotel.mainImage,
            'name': hotel.name,
            'images': [image.image for image in hotel.images.all()],
            'description': hotel.description,
            'rating': hotel.rating,
            'comments': [{
                'id': comment.id,
                'author': {
                    'name': comment.author.name,
                    'email': comment.author.email,
                    'country': comment.author.country,
                    'image': comment.author.image,
                },
                'date': comment.date.strftime("%d/%m/%Y %H:%M:%S"),
                'rating': comment.rating,
                'text': comment.text,
            } for comment in hotel.comments.all()],
            'locatedCountry': hotel.locatedCountry,
            'locatedState': hotel.locatedState,
        }
        for hotel in Hotel.objects.filter(locatedCountry=category)
    ]
    return JsonResponse(hotels, safe=False)


def restaurants(request):
    restaurants = [
        {
            'id': restaurant.pk,
            'mainImage': restaurant.mainImage,
            'name': restaurant.name,
            'price': restaurant.price,
            'caloryInfo': restaurant.caloryInfo,
            'rating': restaurant.rating,
        }
        for restaurant in Restaurant.objects.all()
    ]
    return JsonResponse(restaurants, safe=False)


def destination_category(request):
    categories = set()
    for destination in Destination.objects.all():
        categories.update(destination.category.split())
    return JsonResponse(list(categories), safe=False)


def destinations(request):
    destinations = [
        {
            'id': destination.pk,
            'mainImage': destination.mainImage,
            'images': [image.image for image in destination.images.all()],
            'name': destination.name,
            'description': destination.description,
            'history': destination.history,
            'rating': destination.rating,
            'comments': [{
                'id': comment.id,
                'author': {
                    'name': comment.author.name,
                    'email': comment.author.email,
                    'country': comment.author.country,
                    'image': comment.author.image,
                },
                'date': comment.date.strftime("%d/%m/%Y %H:%M:%S"),
                'rating': comment.rating,
                'text': comment.text,
            } for comment in destination.comments.all()],
            'category': destination.category.split(),
            'locatedCountry': destination.locatedCountry,
            'locatedState': destination.locatedState,
            'overViewVideo': destination.overViewVideo,
        }
        for destination in Destination.objects.all()
    ]
    return JsonResponse(destinations, safe=False)


def destinations_by_category(request, category):
    destinations = [
        {
            'id': destination.pk,
            'mainImage': destination.mainImage,
            'images': [image.image for image in destination.images.all()],
            'name': destination.name,
            'description': destination.description,
            'history': destination.history,
            'rating': destination.rating,
            'comments': [{
                'id': comment.id,
                'author': {
                    'name': comment.author.name,
                    'email': comment.author.email,
                    'country': comment.author.country,
                    'image': comment.author.image,
                },
                'date': comment.date.strftime("%d/%m/%Y %H:%M:%S"),
                'rating': comment.rating,
                'text': comment.text,
            } for comment in destination.comments.all()],
            'category': destination.category.split(),
            'locatedCountry': destination.locatedCountry,
            'locatedState': destination.locatedState,
            'overViewVideo': destination.overViewVideo,
        }
        for destination in Destination.objects.filter(category__contains=category)
    ]
    return JsonResponse(destinations, safe=False)


def destination_state(request):
    categories = set()
    for destination in Destination.objects.all():
        categories.add(destination.locatedState)
    return JsonResponse(list(categories), safe=False)


def destinations_by_state(request, state):
    destinations = [
        {
            'id': destination.pk,
            'mainImage': destination.mainImage,
            'images': [image.image for image in destination.images.all()],
            'name': destination.name,
            'description': destination.description,
            'history': destination.history,
            'rating': destination.rating,
            'comments': [{
                'id': comment.id,
                'author': {
                    'name': comment.author.name,
                    'email': comment.author.email,
                    'country': comment.author.country,
                    'image': comment.author.image,
                },
                'date': comment.date.strftime("%d/%m/%Y %H:%M:%S"),
                'rating': comment.rating,
                'text': comment.text,
            } for comment in destination.comments.all()],
            'category': destination.category.split(),
            'locatedCountry': destination.locatedCountry,
            'locatedState': destination.locatedState,
            'overViewVideo': destination.overViewVideo,
        }
        for destination in Destination.objects.filter(locatedState=state)
    ]
    return JsonResponse(destinations, safe=False)


@csrf_exempt
def comment(request, address, id, user, rating):
    cmnt = Comment.objects.create(author=Profile.objects.get(name=user), rating=float(rating),
                                  text=request.body.decode('utf-8').strip('"'))
    match address:
        case "destination":
            Destination.objects.get(pk=id).comments.add(cmnt)
        case "food":
            Food.objects.get(pk=id).comments.add(cmnt)
        case "hotel":
            Hotel.objects.get(pk=id).comments.add(cmnt)
    return JsonResponse("Success", safe=False)


@csrf_exempt
def login(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    try:
        Profile.objects.get(email=email, password=password)
        return JsonResponse("Success", safe=False)
    except:
        return JsonResponse("Fail", safe=False)


@csrf_exempt
def register(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    name = request.POST.get('name', None)
    country = request.POST.get('country', None)
    try:
        Profile.objects.create(email=email, password=password, name=name, country=country)
        return JsonResponse("Success", safe=False)
    except Exception as e:
        return JsonResponse("Fail", safe=False)
