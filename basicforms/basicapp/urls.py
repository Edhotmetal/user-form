from django.urls import path
from basicapp import views

urlpatterns = [
        path('', views.index, name="index"),
        path('users/', views.users, name="users"),
        path('formpage/', views.formpage, name="form_page"),
        ]
