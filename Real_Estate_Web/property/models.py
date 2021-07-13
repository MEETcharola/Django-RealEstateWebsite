from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

class Property_Images(models.Model):
    image = models.ImageField(upload_to='property_images/sub_images')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.content_type) + "  " + str(self.content_object.title)

from .models import Property_Images


class Property_Residential(models.Model):
    realtor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    property_type = models.CharField(max_length=100, default="Residential", editable=False)
    property_for = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.DecimalField(max_digits=10, decimal_places=0)
    balconies = models.DecimalField(max_digits=10, decimal_places=0)
    bathrooms = models.DecimalField(max_digits=10, decimal_places=0)
    floor_number = models.DecimalField(max_digits=10, decimal_places=0)
    total_floor = models.DecimalField(max_digits=10, decimal_places=0)
    furnishing = models.CharField(max_length=100)
    car_parking = models.DecimalField(max_digits=10, decimal_places=0)
    carpet_area = models.IntegerField()
    super_area = models.IntegerField()
    status = models.CharField(max_length=100)
    photo_main = models.ImageField(default='default.jfif', upload_to='property_images/residential')
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    images = GenericRelation('Property_Images', related_query_name='residential')

    def __str__(self):
        return self.title + " FOR " + self.property_for + " RESIDENTIAL "


class Property_Commercial(models.Model):
    realtor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    property_type = models.CharField(max_length=100, default="Commercial", editable=False)
    property_for = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    landzone = models.CharField(max_length=200)
    ideal_for_business = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    floor_number = models.DecimalField(max_digits=2, decimal_places= 0)
    total_floor = models.DecimalField(max_digits=2, decimal_places= 0)
    washrooms = models.DecimalField(max_digits=2, decimal_places= 0)
    personal_washrooms = models.DecimalField(max_digits=2, decimal_places= 0)
    furnishing = models.CharField(max_length=100)
    cafeteria = models.CharField(max_length=100)
    carpet_area = models.IntegerField()
    super_area = models.IntegerField()
    status = models.CharField(max_length=100)
    photo_main = models.ImageField(default='default.jfif', upload_to='property_images/commercial')
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    images = GenericRelation('Property_Images', related_query_name='commercial')

    def __str__(self):
        return self.title + " FOR " + self.property_for + " COMMERCIAL "


class Property_PG(models.Model):
    realtor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    property_type = models.CharField(max_length=100, default="PG", editable=False)
    property_for = models.CharField(max_length=100, default="PG", editable=False)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=8, decimal_places=2)
    bedrooms = models.DecimalField(max_digits=2, decimal_places= 0)
    balconies = models.DecimalField(max_digits=2, decimal_places= 0)
    bathrooms = models.DecimalField(max_digits=2, decimal_places= 0)
    furnishing = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    photo_main = models.ImageField(default='default.jfif', upload_to='property_images/pg')
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    images = GenericRelation('Property_Images', related_query_name='pg')

    def __str__(self):
        return self.title + " PG "


class Property_Plot(models.Model):
    realtor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    property_type = models.CharField(max_length=100, default="Plot", editable=False)
    property_for = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    floors_allowed_for_construction = models.DecimalField(max_digits=2, decimal_places= 0)
    number_of_openside = models.DecimalField(max_digits=2, decimal_places= 0)
    width_of_road_facing_the_plot = models.IntegerField()
    boundry_wall_status = models.CharField(max_length=100)
    plot_area = models.IntegerField()
    plot_length = models.IntegerField()
    status = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo_main = models.ImageField(default='default.jfif', upload_to='property_images/plot')
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    images = GenericRelation('Property_Images', related_query_name='plot')

    def __str__(self):
        return self.title + " FOR " + self.property_for + " PLOT "



