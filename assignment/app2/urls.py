from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app2'),  # Map the root URL of this app to my_view
]