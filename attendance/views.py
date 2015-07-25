from attendance.models import Attendance
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from login.models import Teacher, Student,Batch

def percentageCalc(listOfRollCalls):
    totalCalls=0
    presentCalls=0
    recentPresentCalls=0  #stores last complete months attendance.
    recentTotalCalls=0

    previousMonth=datetime.date.today().month - 1   #previous month

    for rollCall in listOfRollCalls
        totalCalls+=rollCall.attendanceWeight
        presentCalls+=rollCall.presentPoints
        if rollCall.date.month==previousMonth:
            recentTotalCalls+=rollCall.attendanceWeight
            recentPresentCalls+=rollCall.presentPoints
    return (recentPresentCalls*100.0/recentTotalCalls,presentCalls*100.0/totalCalls)  #overall, lastmonth

@login_required
def home(request):
    #if student, either by database checking or checking post data, yet to be decided.

        #returning average overall and last month attendance, and list of subjects for home page.

        studentbatch_ID=Student.batch_ID  #find students batch id
        responseArray=[]
        for subject in Subjects.objects.filter(batch_ID=studentbatch_ID):
            subWisePercent={}
            allRollCalls=Attendance.objects.filter(student_ID=student_ID, subject_ID=subject.id)
            percentages=percentageCalc(allRollCalls)
            #adding details in dictionary
            subWisePercent['subcode']=Subject.subjectCode
            subWisePercent['subname']=Subject.subjectName
            subWisePercent['monthlyPercentage']=percentages[0]
            subWisePercent['TotalPercentage']=percentages[1]
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
    day_of_week=datetime.datetime.now().isocalendar()[2] #Monday=0, Sunday=7
    date_today=datetime.datetime.now()
    date_start=date_today-datetime.timedelta(days=day_of_week)
    date_end=date_start + datetime.timedelta(days=7)

    studentbatch_ID=Student.batch_ID  #find students batch id
    responseArray=[]
    for subject in Subjects.objects.filter(batch_ID=studentbatch_ID):
        subWisePercent={}
        rollCallWeek=Attendance.objects.filter(student_ID=student_ID, subject_ID=subject.id,,updated__lte=date_end, updated__gt=date_start)
        perc=0
        for rollCall in rollCallWeek:
            totalCalls+=rollCall.attendanceWeight
            presentCalls+=rollCall.presentPoints
        perc=presentCalls*100.0/totalCalls

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


