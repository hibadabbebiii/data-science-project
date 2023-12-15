from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import routers, serializers, viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

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

    print(books.query)  # Add this line to print the generated query
    return render(request, 'home.html', {'books': books})
    # return render(request, 'home.html', {'books': books})



# @csrf_exempt
# @api_view(['POST'])
# def api_login(request):
#     print("Entering api_login view")
#     print("Entering api_login view",request)
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(request, username=username, password=password)
#
#     if user is not None:
#         login(request, user)
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
#     else:
#         return render(request, 'home.html',{'error': 'Invalid credentials'}, status=400)
#
#
# #

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def api_logout(request):
#     logout(request)
#     return JsonResponse({'success': 'Logout successful'})
#


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



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