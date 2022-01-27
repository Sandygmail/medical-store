from django.urls import path

from .views import login, RegisterForm, user_details,user_delete

urlpatterns = [
    path('', login, name="login"),
    path('register', RegisterForm, name="register"),
    path('user_details/', user_details, name="user_details"),
    path('<int:id>/', RegisterForm, name="edit"),
    path('delete/<int:id>/', user_delete, name="delete"),
]
