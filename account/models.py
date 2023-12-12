from django.db import models

# Create your models here.

class EmployeeDetails(models.Model):
    CHOICES = (
  ('25%', '25%'),
  ('50%', '50%'),
  ('75%', '75%'),
  ('100%', '100%')
)
    name = models.CharField(max_length=2332)  
    task = models.CharField(max_length=2332)
    task_date = models.CharField(max_length=255,default='null')
    # from_date = models.DateField(null=True, blank=True)
    # To_date = models.DateField(null=True, blank=True)
    report_of_work = models.CharField(max_length=2332)
    completion_status = models.CharField(choices=CHOICES, max_length=128,default='25%')
    documnet = models.FileField(upload_to='', blank=False, null=True)
    comment = models.CharField(max_length=2332)
    document_base64 = models.TextField(blank=True, null=True)


class LoginProfile(models.Model):
    image = models.ImageField(upload_to='user_images/',blank=False, null=False)
    userid = models.CharField(max_length=20, unique=True,blank=False, null=False)
    name = models.CharField(max_length=100,blank=False, null=False)
    blood_group = models.CharField(max_length=100,blank=False, null=False)
    dob = models.CharField(max_length=100,blank=False, null=False)
    image_base64 = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name


class EmployeeLogin(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # You can adjust the max_length as needed
    name = models.CharField(max_length=2322 , null=False,blank=False,default="") 
    tl = models.BooleanField(default=False)
    testing = models.BooleanField(default=False)
    testing_tl = models.BooleanField(default=False)
    backend = models.BooleanField(default=False)
    backend_tl = models.BooleanField(default=False)






    def __str__(self):
        return self.username


class EmployeeLogin2(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,default='null')
    date = models.CharField(max_length=255,null=True,blank=True)
    login_time = models.CharField(max_length=255,null=True,blank=True)
    longitude1 = models.CharField(max_length=255,null=True,blank=True)
    lattiude1 = models.CharField(max_length=255,null=True,blank=True)
    logout_time = models.CharField(max_length=255,null=True,blank=True)
    longitude2 = models.CharField(max_length=255,null=True,blank=True)
    lattiude2 = models.CharField(max_length=255,null=True,blank=True)
    total_time = models.CharField(max_length=255,null=True,blank=True)






from datetime import datetime
class AssignTask(models.Model):
    assignee_name = models.CharField(max_length=255,null=True,blank=True)
    project_name = models.CharField(max_length=255,null=True,blank=True)
    tl_name = models.CharField(max_length=255,null=True,blank=True)
    task_name = models.CharField(max_length=255,null=True,blank=True)
    due_date  = models.CharField(max_length=255,null=True,blank=True)
    overdue_duedate = models.BooleanField(default=False)
    task_done = models.BooleanField(default=False)
    push_code = models.BooleanField(default=False)
    dev_review = models.BooleanField(default=False)
    add_photo = models.ImageField(upload_to='task_photos/', null=True, blank=True)
    addphoto_base64 = models.TextField(blank=True, null=True)
    task_description = models.TextField(null=True, blank=True)
    testing = models.BooleanField(default=False)
    testing_bug = models.BooleanField(default=False)
    deployment = models.BooleanField(default=False)
    re_deployment = models.BooleanField(default=False)
    re_testing = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if self.due_date:
            due_date_obj = datetime.strptime(self.due_date, '%Y-%m-%d')  # Adjust the format as needed


            if due_date_obj.date() < datetime.now().date():
                self.overdue_duedate = True
            else:
                self.overdue_duedate = False


        super(AssignTask, self).save(*args, **kwargs)


    # def __str__(self):
    #     return self.task_name
    
class AdminAuth(models.Model):
    username=models.CharField(max_length=2322,null=False)
    password =models.CharField(max_length=2322,null=False)
    name=models.CharField(max_length=2322,null=True)



from django.db import models

class EmployeeJoining(models.Model):
    employeeName = models.CharField(max_length=255)
    employeeId = models.CharField(max_length=50)
    totalwork = models.CharField(max_length=50)
    leaves = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    dateOfJoining = models.CharField(max_length=20)
    month = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    basicDA = models.CharField(max_length=50)
    providentFund = models.CharField(max_length=50)
    hra = models.CharField(max_length=50)
    esi = models.CharField(max_length=50)
    conveyance = models.CharField(max_length=50)
    loan = models.CharField(max_length=50)
    professionTax = models.CharField(max_length=50)
    lop = models.CharField(max_length=50)
    totalAddition = models.CharField(max_length=50)
    totalDeduction = models.CharField(max_length=50)
    netSalary = models.CharField(max_length=50)

    # New Field Added
    bankname = models.CharField(max_length=255,null=True,blank=True)
    ifse = models.CharField(max_length=255,null=True,blank=True)
    accnum = models.CharField(max_length=255,null=True,blank=True)
    extrefil1 = models.CharField(max_length=255,null=True,blank=True)
    extrefil2 = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.employeeName
