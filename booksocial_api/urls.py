from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booksocial_api import views


router = DefaultRouter()
router.register('test-viewset',views.TestViewSet,basename='test-viewset')
router.register('profile-viewset',views.UserProfileViewSet)

urlpatterns = [
    path('health_check/', views.HealthCheckView.as_view()),
    path('sayhello/',views.SayHello.as_view()),
    path('',include(router.urls))
]