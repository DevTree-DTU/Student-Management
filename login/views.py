from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model

def saveStudent(request):
    s = Student()
    s.name = request.POST['Name']
    s.address = request.POST['Address']
    s.phoneNo = request.POST['Phone']
    s.fathersName = request.POST['Fathers Name']
    s.DOB = request.POST['DOB']
    s.branch = request.POST['Branch']
    s.admissionYear = request.POST['Year']
    s.email = request.POST['Email']
    #s.isCR = null
    #s.studentID = null
    #s.batchID = null
    s.save()
    response = HttpResponse("Student Saved")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def saveTeacher(request):
    t = Teacher()
    t.name = request.POST['Name']
    t.address = request.POST['Address']
    t.phoneNo = request.POST['Phone']
    t.department = request.POST['Department']
    t.roomNo = request.POST['Room']
    t.designation = request.POST['Designation']
    t.email = request.POST['Email']
    t.dateOfJoining = request.POST['DOJ']
    t.isHOD = request.POST['HOD']
    t.expertise = request.POST['Expertise']
    t.save()
    response = HttpResponse("Teacher Saved")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print('Login Successfull')
            else:
                print('Login Unsuccessful')
        else:
            print('Username/Password do not match')
