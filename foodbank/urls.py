from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'foodbank'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('staff_sign_up/', views.staff_sign_up, name='staff_sign_up'),
    path('staff_login/', views.staff_login_view, name='staff_login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main_page/', views.main_page_view, name='main_page'),
    path('volunteers/', views.VolunteerView.as_view(), name='volunteers'),
    path('foodbanks/', views.FoodBankView.as_view(), name='foodbanks'),
    path('tasks/', views.TaskView.as_view(), name='tasks'),
    path('volunteer_tasks/', views.volunteer_task_view, name='volunteer_tasks'),
    path('volunteer_tasks/delete/', views.volunteer_task_delete, name='volunteer_task_delete'),
    path('vehicles/', views.VehicleView.as_view(), name='vehicles'),
    path('transits/', views.TransitView.as_view(), name='transits'),
    path('fooditems/', views.fooditem_view, name='fooditems'),
    path('fooditems/delete/', views.fooditem_delete, name='fooditem_delete'),
    path('recipient_organizations/', views.recipient_organization_view, name='recipient_organizations'),
    path('recipient_organizations/delete/', views.recipient_organization_delete, name='recipient_organization_delete'),
    path('distributed-food-items/', views.distributed_food_item_view, name='distributed_food_items'),
    path('distributed-food-items/delete/', views.distributed_food_item_delete, name='distributed_food_item_delete'),
    path('donators/', views.donator_view, name='donators'),
    path('donators/delete/', views.donator_delete, name='donator_delete'),
    path('foodgroups/', views.foodgroup_view, name='foodgroups'),
    path('foodgroups/delete/', views.foodgroup_delete, name='foodgroup_delete'),
    path('setup_db/', views.setup_database, name='setup_db')
]
