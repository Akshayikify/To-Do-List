from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup),
    path('login/', views.login_user),
    path('dashboard/', views.dashboard),
    path('edit/<int:task_id>/',views.edit_todo,name='edit')
]
