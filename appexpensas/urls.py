from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="appexpensas"),
    path('add-appexpensas', views.add_expensa,name="add-appexpensas"),
]