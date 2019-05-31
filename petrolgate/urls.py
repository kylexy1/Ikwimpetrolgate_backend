
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'tasks', views.TaskViewSet, base_name='tasks')


urlpatterns = [
 	path('get-all-data', views.getAll),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
