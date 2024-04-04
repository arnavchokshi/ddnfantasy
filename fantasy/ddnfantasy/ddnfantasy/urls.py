"""
URL configuration for ddnfantasy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from users import views as user_views
from comps import views as comp_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("teams/", include("teams.urls")),
    path("leagues/", include("leagues.urls")),
    path("comps/", include("comps.urls")),
    path("realPlacings/", include("realPlacings.urls")),
    path("polls/", include("polls.urls")),
    path('update_top_teams/', views.update_top_teams, name='update_top_teams'),
    path("register/", user_views.register, name='register'),
    path("profile/", user_views.profile, name='profile'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("", views.home_page, name="home_page"),
]
