from attendance.models import Attendance
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from login.models import Teacher, Student,Batch

def percentageRoll(listOfRollCalls):
    totalCalls=0
    presentCalls=0
    for rollCall in listOfRollCalls:
        totalCalls+=rollCall.attendanceWeight
        presentCalls+=rollCall.presentPoints
    return presentCalls*100.0/totalCalls

@login_required
def home(request):
    #if student, either by database checking or checking post data, yet to be decided.

        #returning average overall and last month attendance, and list of subjects for home page.
        previousMonth=datetime.date.today().month - 1   #previous month
        studentbatch_ID=Student.batch_ID  #find students batch id
        responseArray=[]
        for subject in Subjects.objects.filter(batch_ID=studentbatch_ID):
            subWisePercent={}
            allRollCalls=Attendance.objects.filter(student_ID= student_ID, subject_ID=subject.id)
            lastMonthRollCalls=Attendance.objects.filter(student_ID= student_ID, subject_ID=subject.id, timestamp.month = previousMonth)
            percentOverall=percentageRoll(allRollCalls)
            percentLastMonth=percentageRoll(lastMonthRollCalls)
            #adding details in dictionary
            subWisePercent['subcode']=Subject.subjectCode
            subWisePercent['subname']=Subject.subjectName
            subWisePercent['monthlyPercentage']=percentLastMonth
            subWisePercent['TotalPercentage']=percentOverall
            responseArray.append(subWisePercent)


    #elif teacher

        #to show teachers time table. Send whic classes attendance is done and whose is left.

    response = HttpResponse(json.dumps(responseArray), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@login_required
def week_wise(request):
    day_of_week=datetime.datetime.now().isocalendar()[2] #Monday=0, Sunday=7 #gives today's day
    date_today=datetime.datetime.now()  #today's date
    date_start=date_today-datetime.timedelta(days=day_of_week)  #starting of the week
    date_end=date_start + datetime.timedelta(days=7) #

    studentbatch_ID=Student.batch_ID  #find students batch id
    responseArray=[]
    for subject in Subjects.objects.filter(batch_ID=studentbatch_ID):
        subWisePercent={}
        rollCallWeek=Attendance.objects.filter(student_ID=student_ID, subject_ID=subject.id, updated__lte=date_end, updated__gt=date_start)
        perc=0
        perc=percentageRoll(rollCallWeek)

        #adding details in dictionary
        subWisePercent['subcode']=Subject.subjectCode
        subWisePercent['subname']=Subject.subjectName
        subWisePercent['weekPercentage']=perc
        responseArray.append(subWisePercent)

    response = HttpResponse(json.dumps(responseArray), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


@login_required
def month_wise(request):
    pass

@login_required
def date_wise(request):
    pass

@login_required
def subjectPage(request):
    pass

@login_required
def rollCallForBatch(request):
    #selectBatch
    #loadstudents
    #send student names
    #get present/absent/attendance
    #save the records

@login_required
def editAttendanceForBatch(request):
    #selectBatch
    #selectSubject
    #fetch all roll calls
    #send the json


