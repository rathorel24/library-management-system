from django.urls import path
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet,basename="users")

urlpatterns = router.urls