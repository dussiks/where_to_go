from django.urls import path

from map_app import views


urlpatterns = [
    path('', views.show_map)
]
