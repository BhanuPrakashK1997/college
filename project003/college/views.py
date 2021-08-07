from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import StudentApplication, StudentRegistration, StaffRegistration, Department


# Create your views here.
def home(request):
    return render(request, 'college/home.html')


def student_application(request):
    return render(request, 'college/stu_app.html')


def applying(request):
    if request.method == 'POST':
        StudentApplication.objects.create(
            student_name=request.POST['student_name'],
            student_email=request.POST['student_email'],
            ssc_marks=request.POST['ssc_marks'],
            inter_marks=request.POST['inter_marks'])
    return HttpResponseRedirect('/college/student_application/')


def stu_register(request):
    if request.method == 'POST':
        student = StudentApplication.objects.get(student_email=request.POST['email'])
        if student.is_approved:


            username = User.objects.create_user(username=request.POST['username'],
                                                email=request.POST['email'],
                                                password=request.POST['password'],
                                                is_staff='False'
                                                )


            StudentRegistration.objects.create(student=username,
                                             student_app=student,
                                             mobile=request.POST['mobile'],
                                             profile_pic=request.FILES['profile_pic'],
                                             department=Department.objects.get(name=request.POST['department']),
                                             father_name=request.POST['father_name']
                                             )
            return HttpResponseRedirect("/college/home/")
        return HttpResponse("failed")
    return render(request, 'college/stu_register.html')


def stu_login(request):
    return render(request,'college/login.html')


def stu_details(request):
    UserModel = get_user_model()
    # import pdb
    # pdb.set_trace()
    try:
        user = UserModel.objects.get(email = request.POST['email'])
    except UserModel.DoesNotExist:
        return HttpResponse('Student credentials are not correct')
    else:
        if user.check_password(request.POST['password']):
            login(request, user)
            student = StudentRegistration.objects.get(student=user)
            data = {
                "name" :student.student_app.student_name,
                "email":student.student.email,
                "department" :student.department.name,
                "pic" : student.profile_pic,
                "sscmarks" :student.student_app.ssc_marks,
                "intermarks" :student.student_app.inter_marks,
            }
        return render(request,'college/stu_details.html',{'data' : data})
    return HttpResponse('Student credentials are not correct')

def student_list(request):
    list = User.objects.filter(is_staff='False')
    return render(request, 'college/stu_list.html',{"list" : list})





def stu_logout(request):
    logout(request)
    return HttpResponseRedirect('/college/stu_login/')






def staff_register(request):
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        usn = User.objects.create_user(username=request.POST['username'],
                                            email=request.POST["email"],
                                            password=request.POST['password'],
                                            is_staff='True'
                                           )

        StaffRegistration.objects.create(staff=usn,
                                        name=request.POST['name'],
                                        mobile=request.POST['mobile'],
                                        exp=request.POST['exp'],
                                        qualification=request.POST['qualification'],
                                        profile_pic=request.FILES['profile_pic'],
                                        department=Department.objects.get(name=request.POST['department'])
                                        )
        return HttpResponseRedirect('/college/home/')

    return render(request,'college/staff_reg.html')


def staff_login(request):
    return render(request,'college/staff_login.html')

def staff_details(request):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email=request.POST['email'])
    except UserModel.DoesNotExist:
        return HttpResponse('Staff credentials are not correct')
    else:
        if user.check_password(request.POST['password']):
            login(request, user)
            staff = StaffRegistration.objects.get(staff=user)
            staff_data = {
                "name" : staff.name,
                "email" : staff.staff.email,
                "department" : staff.department.name,
                "qualification" : staff.qualification,
                "experience" : staff.exp,
                "mobile" : staff.mobile
            }
            return render(request,"college/staff_details.html",{"staff" : staff_data})
    return HttpResponse('Staff credentials are not correct')

def staff_logout(request):
    logout(request)
    return HttpResponseRedirect("/college/staff_login/")


def staff_list(request):
    staff = User.objects.filter(is_staff="True")
    return render(request, 'college/staff_list.html', {'staff' : staff})

