from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .models import Pizza, UserProfile, User
from django.http import HttpResponse
from django.contrib.auth.models import User

from .serializers import PizzaSerializer, UserProfileSerializer, AdminUserSerializer, EmployeeUserSerializer
from .permissions import IsEmployeeOrNoAccess



class PizzaList(generics.ListCreateAPIView):
   permission_classes = [IsEmployeeOrNoAccess]
   queryset = Pizza.objects.all()
   serializer_class = PizzaSerializer
   
class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = [IsEmployeeOrNoAccess]
   queryset = Pizza.objects.all()
   serializer_class = PizzaSerializer


class UserProfileList(generics.ListCreateAPIView):
   permission_classes = [IsEmployeeOrNoAccess]
   queryset = UserProfile.objects.all()
   serializer_class = UserProfileSerializer

# def perform_create():
#       if UserProfile.isEmployee:
#          return AdminUserSerializer
#       return EmployeeUserSerializer


class UserList(generics.ListCreateAPIView):
   permission_classes = [IsAdminUser]
   queryset = User.objects.all()
   serializer_class = EmployeeUserSerializer

   
   

