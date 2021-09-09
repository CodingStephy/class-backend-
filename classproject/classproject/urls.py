from django.urls import path, include
from rest_framework import routers
from classes.views import ClassViewSet

# create the router
router = routers.DefaultRouter()
# register our viewsets

router.register(r'class', ClassViewSet) 
print(router)


urlpatterns = [
    path("", include(router.urls))
]