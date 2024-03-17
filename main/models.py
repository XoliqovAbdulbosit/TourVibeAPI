from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=40)
    image = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey('Profile', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    text = models.TextField()

    def __str__(self):
        return self.author.name


class Destination(models.Model):
    mainImage = models.CharField(max_length=120)
    images = models.ManyToManyField(Image)
    name = models.CharField(max_length=40)
    description = models.TextField()
    history = models.TextField()
    comments = models.ManyToManyField(Comment, blank=True)
    category = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    locatedCountry = models.CharField(max_length=20)
    locatedState = models.CharField(max_length=20)
    overViewVideo = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    mainImage = models.CharField(max_length=120)
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=20)
    caloryInfo = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    overViewVideo = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    mainImage = models.CharField(max_length=120)
    images = models.ManyToManyField(Image)
    name = models.CharField(max_length=40)
    description = models.TextField()
    comments = models.ManyToManyField(Comment, blank=True)
    category = models.CharField(max_length=20)
    locatedCountry = models.CharField(max_length=20)
    locatedState = models.CharField(max_length=20)
    restaurant = models.ManyToManyField(Restaurant, blank=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    mainImage = models.CharField(max_length=120)
    name = models.CharField(max_length=40)
    images = models.ManyToManyField(Image)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    comments = models.ManyToManyField(Comment, blank=True)
    locatedCountry = models.CharField(max_length=20)
    locatedState = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40, unique=True)
    number = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=20)
    image = models.CharField(max_length=120, blank=True)
    savedDestinations = models.ManyToManyField(Destination, blank=True)
    savedFoods = models.ManyToManyField(Food, blank=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name
