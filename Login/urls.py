from django.urls import path
from Login import views



urlpatterns= [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/',views.user_login, name='userlogin'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
]