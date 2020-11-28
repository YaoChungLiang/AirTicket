from django.urls import path
from flight import views

urlpatterns = [
    path('', views.sample, name='home'),
    path('home/', views.sample, name='home'),
    path('<age>/',views.get_info, name='getInfo')
]