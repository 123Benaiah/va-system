from django.urls import path
from . import views

app_name = 'va'

urlpatterns = [
    path('', views.home, name='home'),
    path('records/', views.record_list, name='record_list'),
    path('records/add/', views.add_record, name='add_record'),
]

