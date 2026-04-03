from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup),
    path('login/', views.login_user),
    path('dashboard/', views.dashboard),
    path('edit/<int:task_id>/',views.edit_todo,name='edit'),
    path('delete/<int:task_id>/',views.delete_todo,name='delete'),
    path('logout/',views.logout_user,name="logout"),
]
