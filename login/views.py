from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from login.models import Student, Teacher
import json
def saveStudent(request):
    try:
        s = Student()
        s.username = request.POST['Username']
        s.password = request.POST['Password']
        s.name = request.POST['Name']
        s.address = request.POST['Address']
        s.phoneNo = request.POST['Phone']
        s.fathersName = request.POST['FathersName']
        s.DOB = request.POST['DOB']
        s.branch = request.POST['Branch']
        s.admissionYear = request.POST['Year']
        s.email = request.POST['Email']
        s.isCR = 'False'
        s.studentID = s.username
        s.batchID = 'A6'
        s.save()
    except Exception as e:
        #responseArray = []
        data = {}
        data['Status'] = 0
        data['Description'] = str(e)
        #responseArray.append(data)
        response = HttpResponse(json.dumps(data), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    #responseArray = []
    data = {}
    data['Status'] = int(1)
    data['Description'] = 'Registration Successful'
    #responseArray.append(data)
    response = HttpResponse(json.dumps(data), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
#    response = HttpResponse("Student Saved")
#    response["Access-Control-Allow-Origin"] = "*"
def saveTeacher(request):
    try:
        t = Teacher()
        t.username = request.POST['Username']
        t.password = request.POST['Password']
        t.name = request.POST['Name']
        t.address = request.POST['Address']
        t.department = request.POST['Department']
        t.phoneNo = request.POST['Phone']
        t.roomNo = request.POST['Room']
        t.designation = request.POST['Designation']
        t.email = request.POST['Email']
        t.dateOfJoining = request.POST['DOJ']
        t.isHOD = request.POST['HOD']
        t.expertise = request.POST['Expertise']
        t.save()
    except Exception as e:
        #responseArray = []
        data = {}
        data['Status'] = 0
        data['Description'] = str(e)
        #responseArray.append(data)
        response = HttpResponse(json.dumps(data), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    #responseArray = []
    data = {}
    data['Status'] = int(1)
    data['Description'] = 'Registration Successful'
    #responseArray.append(data)
    response = HttpResponse(json.dumps(data), content_type="application/json")

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
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
                data = {}
                data['Status'] = int(1)
                data['Description'] = 'Login Successful'
                response = HttpResponse(json.dumps(data), content_type="application/json")
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Headers"] = "*"
                return response
            else:
                data = {}
                data['Status'] = int(0)
                data['Description'] = 'Login Unsuccessful'
                response = HttpResponse(json.dumps(data), content_type="application/json")
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Headers"] = "*"
                return response
        else:
            data = {}
            data['Status'] = int(0)
            data['Description'] = 'Username not found'
            response = HttpResponse(json.dumps(data), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Headers"] = "*"
            return response
    else:
        data = {}
        data['Status'] = int(0)
        data['Description'] = 'POST Requests only'
        response = HttpResponse(json.dumps(data), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        return response

def getStudents(request):
    batch = ''
    if request.POST:
        batch = request.POST.get('batch')
        try:
            responseArray = []
            flag = 10
            for student in Student.objects.all():
                if student.batchID == batch:
                    if flag == 10:
                        data = {}
                        data['Status'] = 1
                        data['Description'] = 'Successful'
                        responseArray.append(data)
                        flag = 1
                    data = {}
                    data['Name'] = student.name
                    data['Address'] = student.address
                    data['PhoneNo'] = student.phoneNo
                    data['Email'] = student.email
                    data['FathersName'] = student.fathersName
                    data['DOB'] = str(student.DOB)
                    data['BatchID'] = student.batchID
                    data['Branch'] = student.branch
                    data['AdmissionYear'] = student.admissionYear
                    responseArray.append(data)
            if flag != 1:
                data = {}
                data['Status'] = 0
                data['Description'] = 'No Student Found'
                responseArray.append(data)
            response = HttpResponse(json.dumps(responseArray), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        except Exception as e:
            data = {}
            data['Status'] = 0
            data['Description'] = str(e)
            #responseArray.append(data)
            response = HttpResponse(json.dumps(data), content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "*"
            return response
    else:
        data = {}
        data['Status'] = int(0)
        data['Description'] = 'POST Requests only'
        response = HttpResponse(json.dumps(data), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        return response
