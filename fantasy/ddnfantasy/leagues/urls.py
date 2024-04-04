from django.urls import path
from leagues import views

urlpatterns = [
    path('', views.my_leagues, name='my_leagues'),
    path('create/', views.create_league, name='create_league'),
    path('join/', views.join_league, name='join_league'),
    path('details/<int:league_id>/', views.league_details, name='league_details'),

    # Add more URLs as needed
]
