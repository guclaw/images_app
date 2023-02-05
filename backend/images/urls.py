from django.urls import path
from rest_framework.routers import SimpleRouter

from images import views

app_name = 'images'

router = SimpleRouter()
router.register(r'images', views.ImageViewSet, basename='images')

urlpatterns = router.urls