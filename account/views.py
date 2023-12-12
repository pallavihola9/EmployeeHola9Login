from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
import base64
from rest_framework import status
from django.http import JsonResponse
from rest_framework import generics 


# Create your views here.
# add limit parameter for GET method only

class EmployeeProfileView(generics.ListCreateAPIView):
    serializer_class = EmployeeDetailsSerializer
    def get_queryset(self):
        limit = self.request.data.get('limit')
        if limit is not None:
            return EmployeeDetails.objects.all().order_by('-id')[:int(limit)]
        else:
            return EmployeeDetails.objects.all()
        
        # serializer = EmployeeDetailsSerializer(emp_profile,many=True)
        # return Response(serializer.data)
      
class LoginProfileList(generics.ListCreateAPIView):
    serializer_class = LoginProfileSerializer
    def get_queryset(self):
        # Retrieve all user profiles
        # Add new code with limit parameter
        name = self.request.data.get('name')
        limit = self.request.data.get('limit')
        if limit is not None:
            return LoginProfile.objects.all().order_by('-id')[:int(limit)] if limit else LoginProfile
        else:
            return LoginProfile.objects.filter(name__icontains=name) if name \
                    else LoginProfile.objects.all()

        # serializer = LoginProfileSerializer(profiles, many=True)
        # return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = LoginProfileSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'image' in request.data:
                # Get the uploaded file
                uploaded_file = request.data['image']

                # Convert the file to base64
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                # Update the serializer's data to store the base64 encoded document
                serializer.validated_data['image_base64'] = base64_encoded

            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginProfileDetail(APIView):
    def get_object(self, pk):
        try:
            return LoginProfile.objects.get(pk=pk)
        except LoginProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # Retrieve a single user profile
        profile = self.get_object(pk)
        serializer = LoginProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = LoginProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'image' in request.data:
                uploaded_file = request.data['image']
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                serializer.validated_data['image_base64'] = base64_encoded

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeLogin
from django.http import HttpResponse

class EmployeeLoginView(generics.ListCreateAPIView):
    serializer_class = EmployeeLoginSerializer
    def post(self,request,format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        name = request.data.get("name")
        x = EmployeeLogin.objects.filter(username=username).filter(password=password).filter(name=name)
        if x:
            return HttpResponse("true", content_type='application/json')
        else:
            return HttpResponse("false", content_type='application/json')
        
        # add limit parameter####
    def get_queryset(self):
        limit = self.request.data.get('limit')
        if limit is not None:
            return EmployeeLogin.objects.all().order_by('-id')[:int(limit)]
        else:
            return  EmployeeLogin.objects.all()
        # employees = EmployeeLogin.objects.all()
        # serializer = EmployeeLoginSerializer(employees, many=True)
        # return Response(serializer.data)
     
        
import base64
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EmployeeDetails
from .serializers import EmployeeDetailsSerializer

class EmployeeDetailsView(APIView):
    def post(self, request, format=None):
        serializer = EmployeeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'documnet' in request.data:
                # Get the uploaded file
                uploaded_file = request.data['documnet']

                # Convert the file to base64
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                # Update the serializer's data to store the base64 encoded document
                serializer.validated_data['document_base64'] = base64_encoded

            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
class EmployeeLoginView2(APIView):
    def get(self, request):
        # New Code#
        name = request.data.get('name')
        limit = request.data.get('limit')
        
        employees =EmployeeLogin2.objects.filter(name__icontains=name) if name \
                   else EmployeeLogin2.objects.all()  
        # Add limits 
        employees = employees[:int(limit)] if limit else employees  

        serializer = EmployeeLogin2Serializer2(employees, many=True)
        return Response(serializer.data)
    

     
    def post(self, request):
        serializer = EmployeeLogin2Serializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class  EmployeeLoginUpdateDelete2(APIView):
    def put(self,request,pk):
        employee2 = EmployeeLogin2.objects.get(pk=pk)
        serializer = EmployeeLogin2Serializer2(employee2,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self,request,pk):
        employee_login = EmployeeLogin2.objects.get(pk=pk)
        employee_login.delete()
        return Response({"message": "deleted successfully."},status=status.HTTP_204_NO_CONTENT)
   
class AssignTaskView(generics.ListCreateAPIView):
    
    serializer_class = AssignTaskSerializer 

    def get_queryset(self):
        # New Code 
        assignee_name = self.request.data.get('assignee_name')
        tl_name = self.request.data.get('tl_name')
        limit = self.request.data.get('limit')
        if limit is not None:
            return AssignTask.objects.all().order_by('-id')[:int(limit)] if limit else AssignTask
        else:
            return AssignTask.objects.filter(assignee_name__icontains=assignee_name, tl_name__icontains=tl_name) if assignee_name and tl_name \
                    else AssignTask.objects.filter(assignee_name__icontains=assignee_name) if assignee_name \
                    else AssignTask.objects.all()
        
        # serializer = AssignTaskSerializer(assign_task, many=True)
        # return Response(serializer.data)
 
    def post(self, request):
        serializer = AssignTaskSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'add_photo' in request.data:
                # Get the uploaded file
                uploaded_file = request.data['add_photo']

                # Convert the file to base64
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                # Update the serializer's data to store the base64 encoded document
                serializer.validated_data['addphoto_base64'] = base64_encoded

            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class  AssignTaskUpdateDelete(APIView):
    def put(self,request,pk):
        assign_task = AssignTask.objects.get(pk=pk)
        serializer = AssignTaskSerializer(assign_task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self,request,pk):
        assign_task = AssignTask.objects.get(pk=pk)
        assign_task.delete()
        return Response({"message": "deleted successfully !"},status=status.HTTP_204_NO_CONTENT)
    
class adminAuth(APIView):
    def post( self,request, format=None):
        username =request.data.get("username")
        password=request.data.get("password")
        s=AdminAuth.objects.filter(username=username).filter(password=password)
        if s:
            return HttpResponse("true", content_type='application/json')
        else:
            return HttpResponse("false", content_type='application/json') 
        


class EmployeeJoiningListView(generics.ListCreateAPIView):
    serializer_class = EmployeeJoiningSerializer
    def get_queryset(self):
        limit = self.request.data.get('limit')
        if limit is not None:
            return EmployeeJoining.objects.all().order_by('-id')[:int(limit)]
        else:
            return EmployeeJoining.objects.all()
        # serializer = EmployeeJoiningSerializer(employees, many=True)
        # return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeJoiningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeJoiningDetailView(APIView):
    def get(self, request, pk):
        employee = EmployeeJoining.objects.get(pk=pk)
        serializer = EmployeeJoiningSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = EmployeeJoining.objects.get(pk=pk)
        serializer = EmployeeJoiningSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = EmployeeJoining.objects.get(pk=pk)
        employee.delete()
        return Response({"message": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

