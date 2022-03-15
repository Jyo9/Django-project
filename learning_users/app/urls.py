from django.urls import URLPattern, path
from  app import views

urlpatterns =[
    path('',views.index,name = 'index'),
    path('register/',views.register,name='register'),
    path('special/',views.special,name='special'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),
]