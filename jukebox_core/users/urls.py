from django.urls import path
from jukebox_core.users import views
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]