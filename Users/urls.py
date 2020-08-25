from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.CreateUser.as_view(), name='create_user'),
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name='profile'),
]