from django.urls import path
from jukebox_core.pages import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]