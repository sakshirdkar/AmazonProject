from django.urls import path
from . import views

# Define our API
urlpatterns = [
    path('amazonservice/', views.index)
]
