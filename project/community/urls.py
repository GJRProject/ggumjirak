from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('schedule/', views.schedule),
    path('alpha/', views.alpha),
    path('beta/', views.beta),
    path('gamma/', views.gamma)

]