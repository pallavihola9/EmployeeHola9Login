from django.urls import path
from .views import  *
from account.views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('employeeprofile/', EmployeeProfileView.as_view(), name='employeeprofile'),#done
     path('loginprofile/', LoginProfileList.as_view(), name='loginprofile'),# done
     path('loginprofile/<int:pk>/', LoginProfileList.as_view(), name='loginprofile'), #new url added
     path('loginprofile/<int:pk>/', LoginProfileDetail.as_view(), name='profile-detail'),
     path('loginEmployee/', EmployeeLoginView.as_view(), name='loginEmployee'),#done
     path('detailEmployee/', EmployeeDetailsView.as_view(), name='detailEmployee'),#done
     path('employeelogin2',EmployeeLoginView2.as_view(), name='employeelogin2'),# done
     path('employeelogin2/<int:pk>',EmployeeLoginUpdateDelete2.as_view(), name='employeelogin2'),# done
     path('assigntaskview',AssignTaskView.as_view(), name='assigntaskview'), # done
     path('assigntaskview/<int:pk>',AssignTaskUpdateDelete.as_view(), name='assigntaskview'), # done
     path('adminAuth', adminAuth.as_view(),name='adminAuth'), # done
     
     path('employees_joining/', EmployeeJoiningListView.as_view(), name='employees_joining'),
     path('employees_joining/<int:pk>/', EmployeeJoiningDetailView.as_view(), name='employees_joining-detail'),

   
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)