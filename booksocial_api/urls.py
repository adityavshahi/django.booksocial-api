from django.urls import path
from booksocial_api import views

urlpatterns = [
    path('health_check/', views.HealthCheckView.as_view()),
    path('sayhello/',views.SayHello.as_view())
]