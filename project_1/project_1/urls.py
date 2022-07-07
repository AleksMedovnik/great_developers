from django.contrib import admin
from django.urls import path
from blog.views import PersonAPIViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/personList/', PersonAPIViews.as_view()),
    path('api/v1/personList/<int:pk>/', PersonAPIViews.as_view())
]