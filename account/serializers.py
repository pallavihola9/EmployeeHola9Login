from rest_framework import serializers
from .models import *

class EmployeeLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLogin
        fields = '__all__'


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'
        

class LoginProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginProfile
        fields = '__all__'
        
class EmployeeLogin2Serializer2(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLogin2
        fields = '__all__'
        
class AssignTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignTask
        fields = '__all__'


class EmployeeJoiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeJoining
        fields = '__all__'