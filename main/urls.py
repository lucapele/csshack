from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('commenta', views.CreaCommento.as_view())
]
