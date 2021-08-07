from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department_choices =(('ECE','Electroonics and communication'),
                         ('MECH','Mechanical'))
    name = models.CharField(max_length=10,choices=department_choices)

    def __str__(self):
        return self.name


class StudentApplication(models.Model):
    student_name = models.CharField(max_length=150)
    student_email = models.EmailField(unique= True)
    ssc_marks = models.IntegerField()
    inter_marks = models.IntegerField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name


class StudentRegistration(models.Model):
    student = models.OneToOneField(User,on_delete=models.CASCADE)
    student_app = models.OneToOneField(StudentApplication, on_delete= models.CASCADE)
    mobile = models.IntegerField()
    department = models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    profile_pic = models.ImageField(upload_to="images/")
    father_name = models.CharField(max_length=150)




class StaffRegistration(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    mobile = models.IntegerField()
    exp = models.IntegerField()
    qualification = models.CharField(max_length=140)
    profile_pic = models.ImageField(upload_to="images/")
    department = models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.staff

