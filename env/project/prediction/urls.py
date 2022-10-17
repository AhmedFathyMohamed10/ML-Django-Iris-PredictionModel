from django.urls import path
from . import views

urlpatterns = [
    path("", views.predict_view, name="predict_view"),
    path("result/", views.result_view, name="result_view"),
    path("predict/", views.predict_chances, name="predict_chances"),
]