from hello_app.views import HomeWorldView, HomeView
from django.urls import path

urlpatterns = [
    path('world', view = HomeWorldView.as_view()),
    path('<str:name>', view = HomeView.as_view())
]