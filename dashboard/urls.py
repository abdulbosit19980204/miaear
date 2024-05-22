from django.urls import path
from .views import home_view, user_home_view, channels_view, users_view

urlpatterns = [
    path('', home_view),
    path('user/', user_home_view),
    path('users/', users_view),
    path('channels/', channels_view),
]
