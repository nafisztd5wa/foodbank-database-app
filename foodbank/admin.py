from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Volunteer, FoodBank, Task, Volunteer_Task, Vehicle, TransitSchedule, FoodItem, DistributedFoodItem, RecipientOrganization

admin.site.register(Volunteer)
admin.site.register(FoodBank)
admin.site.register(Task)
admin.site.register(Volunteer_Task)
admin.site.register(Vehicle)
admin.site.register(TransitSchedule)
admin.site.register(FoodItem)
admin.site.register(DistributedFoodItem)
admin.site.register(RecipientOrganization)
