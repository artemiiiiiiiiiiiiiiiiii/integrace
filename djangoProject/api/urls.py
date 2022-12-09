from django.urls import path
from . import views

urlpatterns = [
    path('<str:my_word>', views.ReplaceView.as_view(), name="replace"),
]