from django.urls import path
from basicapp import views

# app_name for relative file paths
app_name = 'basicapp'

urlpatterns = [
        path('', views.index, name="index"),
        path('users/', views.users, name="users"),
        path('formpage/', views.formpage, name="form_page"),
        ]
