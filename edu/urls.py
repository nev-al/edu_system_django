from django.urls import path

from . import views

urlpatterns = [
    path("available_products", views.available_products, name="available_products"),
    path("<str:uid>/", views.lessons, name="lessons"),
    path("statistics", views.statistics, name="stat"),
]
