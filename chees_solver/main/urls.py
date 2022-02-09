from django.urls import path
from .views import index, start, validate_move_for_chess

urlpatterns = [
    path("", start),
    path("<str:figure>/<str:fild>", index),
    path("<str:figure>/<str:fild>/<str:second>", validate_move_for_chess),
]
