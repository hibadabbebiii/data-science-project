from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import routers, serializers, viewsets
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from bson import ObjectId  # Import ObjectId from the bson module
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import *
import pymongo
import pandas as pd
from rest_framework.response import Response

# Create your views here.

from django.http import HttpResponse
from .models import *
def home(request):
    return render(request,'home.html',{})
def say_hello(request):
    return HttpResponse('HELLO World')

def get_books(request):
    books = Books.objects.all()
    person = Person.objects.all()

  # Add this line to print the generated query
    return render(request, 'home.html', {'books': books})
    # return render(request, 'home.html', {'books': books})

def get_bookswithgenre(request, genre=None):
    if genre:
        books = Books.filter_by_genre(genre)
    else:
        books = Books.objects.all()

    return render(request, 'home.html', {'books': books})




def get_bookswithLimit(request, genre=None):
    if genre:
        # Assuming 'genre' is a field in your Book model
        books = Books.objects.filter(genre=genre)[:10]
        book_count = Books.objects.filter(genre=genre).count()
    else:
        books = Books.objects.all()[:10]
        book_count = Books.objects.all().count()

    return render(request, 'home.html', {'books': books, 'book_count': book_count})

def get_book_by_id(request, book_id):
    print("testttttttttttttttttttttt")
    try:
        # Convert the string representation of ObjectId to ObjectId
        book = Books.objects.get(book_id=book_id)
    except Books.DoesNotExist:
        return HttpResponseNotFound("Book not found")

    return render(request, 'book_detail.html', {'book': book})





@csrf_exempt
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_login(request):
    print("Entering api_login view")
    print("Entering api_login view",request)
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    else:
        return render(request, 'home.html',{'error': 'Invalid credentials'}, status=400)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    logout(request)
    return JsonResponse({'success': 'Logout successful'})



@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def user_login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#
#     user = authenticate(request, username=username, password=password)
#
#     if user is not None:
#         login(request, user)
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
#     else:
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#


# def dataframe(request):
#
#     # Retrieve data from the MongoDB "books" collection
#     books_data = []
#     for x in Books.objects.find():
#         books_data.append(x)
#
#     # Convert data to a Pandas DataFrame
#     visual_data = pd.DataFrame.from_dict(books_data)
#
#     return render(request,  'home.html',{'visual_data': visual_data})