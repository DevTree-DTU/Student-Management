from django.shortcuts import render
from login.models import Teacher, Student,Batch
from attendance.models import Attendance
import datetime
import json

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
    return (recentPresentCalls*100.0/recentTotalCalls,presentCalls*100.0/totalCalls)

def home(request):
    #if student
        studentBatchId=Student.batchID  #find students batch id
        responseArray=[]
        for subject in Subjects.objects.filter(batchID=studentBatchId):
            subWisePercent={}
            allRollCalls=Attendance.objects.filter(studentID=studentId, subjectID=subject.id)
            percentages=percentageCalc(allRollCalls)
            #adding details in dictionary
            subWisePercent['subcode']=Subject.subjectCode
            subWisePercent['subname']=Subject.subjectName
            subWisePercent['monthlyPercentage']=percentages[0]
            subWisePercent['TotalPercentage']=percentages[1]
            responseArray.append(subWisePercent)

        response = HttpResponse(json.dumps(responseArray), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

def studentPercentage(request):
    pass

def rollCallForBatch(request):
    #selectBatch
    #loadstudents
    #send student names
    #get present/absent/attendance
    #save the records

def editAttendanceForBatch(request):
    #selectBatch
    #selectSubject
    #fetch all roll calls
    #send the json


