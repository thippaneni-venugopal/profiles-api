from django.urls import path, include
from profiles_api import views


urlpatterns = [
  path('hello/', views.HelloApiView.as_view()),
]