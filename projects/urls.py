from django.urls import path, include
from rest_framework import routers
from projects import views

router = routers.DefaultRouter()
router.register(r'adquisiciones',views.AdquisicionViewSet)

urlpatterns=[
    path('',include(router.urls))
]