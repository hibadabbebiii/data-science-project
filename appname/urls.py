from django.urls import path
from . import views

#urlConfig

urlpatterns = [

   path('hello/',views.say_hello),
   path('',views.home),
   path('books/', views.get_books),
   path('login/',  views.user_login),
   # path('api_login/', views.api_login, name='api_login'),

   # path('logout/',  views.api_logout),
   path('register/', views.register_user, name='register_user')

]

