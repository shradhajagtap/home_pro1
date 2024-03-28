from django.urls import path
from .views import india_info, show_view, delete_view, update_view

urlpatterns = [
    path("", india_info, name="india_url"),
    path("show/", show_view, name="show_url"),
    path("update/<int:pk>", update_view, name="update_url"),
    path("delete/<int:pk>", delete_view, name="delete_url")
]
