from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('schedule/', views.schedule),
    path('donation/', views.donation),
    path('beta/', views.beta),
    path('gamma/', views.gamma),
    path('blog/', views.blog),
    path('blog/<int:pk>/',views.posting, name='posting'),
    path('contact/', views.contact),
    path('board/', views.board),
    path('gallery/', views.gallery),
    path('ci/', views.ci),
    path('greeting/', views.greeting),
]