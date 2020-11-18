from django.urls import path
from .views import StartupListAPIView,StartupDetailAPIView


urlpatterns = [
    path('startups/', StartupListAPIView.as_view()),
    path('startup/<slug:slug>/', StartupDetailAPIView.as_view()),
    path('startup/', StartupDetailAPIView.as_view()),
]