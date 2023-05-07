from django.urls import path, include
from .views import user_view, home

urlpatterns = [
    path('user_view/', user_view, name='user_view'),
    path('home/', home, name='home')
]