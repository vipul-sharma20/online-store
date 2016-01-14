from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers
import app
from app import views, urls
from django.conf.urls import include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(app.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
