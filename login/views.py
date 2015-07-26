from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from login.models import Student, Teacher
def saveStudent(request):
    s = Student()
    s.username = request.POST['Username']
    s.password = request.POST['Password']
    s.name = request.POST['Name']
    s.address = request.POST['Address']
    s.phoneNo = request.POST['Phone']
    s.fathersName = request.POST['Fathers Name']
    s.DOB = request.POST['DOB']
    s.branch = request.POST['Branch']
    s.admissionYear = request.POST['Year']
    s.email = request.POST['Email']
    s.isCR = 'False'
    s.studentID = s.username
    s.batchID = 'A6'
    s.save()
    response = HttpResponse("Student Saved")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def saveTeacher(request):
    t = Teacher()
    s.username = request.POST['Username']
    s.password = request.POST['Password']
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
                response = HttpResponse('Login Successful')
                response["Access-Control-Allow-Origin"]
                return response
            else:
                response = HttpResponse('Login Unsuccessful')
                response["Access-Control-Allow-Origin"]
                return response
        else:
            response = HttpResponse('Login Unsuccessful')
            response["Access-Control-Allow-Origin"]
            return response
