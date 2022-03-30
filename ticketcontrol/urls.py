"""ticketcontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

app_name="ticketcontrol"
urlpatterns = [
    # path('admin/', admin_view),
    path('ticket/my', mytickets_view),
    path('ticket/<int:id>', ticket_view),
    # path('ticket/new', new_ticket_view),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user/create', create_user_view, name='create_user'),
    path('user/<int:id>', user_details_view, name='user_details'),
    path('user/<int:id>/edit', edit_user_view, name='edit_user'),
    path('user/<int:id>/delete', delete_user_view, name='delete_user'),
    path('user/profile', profile_view, name='profile'),
    path('user/manage', manage_users_view, name='manage_users'),
    path('group/manage', manage_groups_view, name='manage_groups'),
    path('group/create', create_group_view, name='create_group'),
    path('group/<int:id>/delete', delete_group_view, name='delete_group'),
    path('group/<int:id>', edit_group_view, name='edit_group'),
    path('djangoadmin/', admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path('home/', home_view, name='home'),
]

handler404 = "ticketcontrol.views.handler404"