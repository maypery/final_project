from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api_app', views.EmployeeView)
app_name = "api"
urlpatterns = [
    path('', include(router.urls),),
]