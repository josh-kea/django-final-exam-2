from rest_framework import serializers
from .models import Pizza, UserProfile, User
from rest_framework.fields import CurrentUserDefault

class PizzaSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__' # all model fields will be included
      model = Pizza

class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__' # all model fields will be included
      model = UserProfile

class AdminUserSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__' # all model fields will be included
      model = User

class EmployeeUserSerializer(serializers.ModelSerializer):
   class Meta:
      fields = ['id', 'username', 'email', 'date_joined', "is_staff"] # all model fields will be included
      model = User



