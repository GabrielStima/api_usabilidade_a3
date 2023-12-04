from django.urls import path
from .views import StoreViewset, StoreViewset_UUID
from rest_framework import routers

app_name = 'stores'

router = routers.DefaultRouter()


urlpatterns = [
    path('stores/', StoreViewset.as_view()),
    path('stores/store/<uuid:pk>', StoreViewset_UUID.as_view())
]