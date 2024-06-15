from django.db import models
from datetime import datetime

class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    home_state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class FoodBank(models.Model):
    id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    home_state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20, default="00000")
    manager = models.ForeignKey(Volunteer, on_delete=models.PROTECT, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    start_date_time = models.DateTimeField(default=datetime.strptime('2000-01-01 09:00:00', "%Y-%m-%d %H:%M:%S"))
    end_date_time = models.DateTimeField(default=datetime.strptime('2000-01-01 12:00:00', "%Y-%m-%d %H:%M:%S"))
    associated_food_bank = models.ForeignKey(FoodBank, on_delete=models.CASCADE, null=True, blank=True)
    min_volunteers = models.IntegerField(default=0)
    max_volunteers = models.IntegerField(default=10)

class Volunteer_Task(models.Model):
    id = models.AutoField(primary_key=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    driver_volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_type = models.CharField(max_length=255, default="")
    total_passenger_capacity = models.IntegerField(default=0)

class TransitSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    arrival_date_time = models.DateTimeField(default=datetime.strptime('2000-01-01 09:00:00', "%Y-%m-%d %H:%M:%S"))
    departure_date_time = models.DateTimeField(default=datetime.strptime('2000-01-01 12:00:00', "%Y-%m-%d %H:%M:%S"))
    current_available_capacity = models.IntegerField(default=0)

class Donator(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

class FoodGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
class FoodItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    food_group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
    expiration_date = models.DateField()
    item_size = models.CharField(max_length=255)
    associated_food_bank = models.ForeignKey(FoodBank, on_delete=models.CASCADE, null=True, blank=True)
    donator = models.ForeignKey(Donator, on_delete=models.CASCADE)


class DistributedFoodItem(models.Model):
    id = models.AutoField(primary_key=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, null=True, blank=True)
    recipient_org = models.ForeignKey('RecipientOrganization', on_delete=models.CASCADE, null=True, blank=True)

class RecipientOrganization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    home_state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
