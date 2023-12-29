from django.urls import path
from . import views

#urlConfig

urlpatterns = [

   path('hello/',views.say_hello),
   path('',views.home),
   path('books/', views.get_books),
   path('get_bookswithgenre/', views.get_bookswithgenre),
   path('books/<str:genre>/', views.get_bookswithgenre, name='get_books_by_genre'),
   path('bookswithLimit/<str:genre>/', views.get_bookswithLimit),
   path('getbookby/<int:book_id>/', views.get_book_by_id),

   # path('login/',  views.user_login),
   # path('api_login/', views.api_login, name='api_login'),

   # path('logout/',  views.api_logout),
   # path('register/', views.register_user, name='register_user')

]

