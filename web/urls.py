from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.list_users),
    path('users/create/', views.create_user),
    path('users/delete/<int:pk>/', views.delete_user),
]
