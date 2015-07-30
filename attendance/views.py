from attendance.models import Attendance
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from login.models import Teacher, Student,Batch

days_months=[31,28,31,30,31,30,31,31,30,31,30,31]
days_months_leap=[31,29,31,30,31,30,31,31,30,31,30,31]

def increment_month_start(dateobj):
    if dateobj.year % 4 == 0 :
        dateobj=dateobj+datetime.timedelta(days=days_months_leap[dateobj.month - 1])
    else :
        dateobj=dateobj+datetime.timedelta(days=days_months[dateobj.month - 1])

def increment_month_end(dateobj):
    if dateobj.year % 4 == 0 :
        dateobj=dateobj+datetime.timedelta(days=days_months_leap[dateobj.month])
    else :
        dateobj=dateobj+datetime.timedelta(days=days_months[dateobj.month])

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

        #to show teachers time table. Send which classes attendance is done and whose is left.

    response = HttpResponse(json.dumps(responseArray), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@login_required
def week_wise(request, offset):
    #offset as provided in url
    if offset < 0 :
        return render(request, 'error.html', {'error': True})

    day_of_week=datetime.datetime.now().isocalendar()[2] #Monday=0, Sunday=7 #gives today's day
    date_today=datetime.datetime.now()  #today's date
    date_start=date_today-datetime.timedelta(days=day_of_week+(7*offset))  #starting of the week
    date_start = date_start.replace(hour=0, minute=0)
    date_end=date_start + datetime.timedelta(days=7)  #week end

    studentbatch_ID=Student.batch_ID  #find students batch id
    responseArray=[]
    for subject in Subjects.objects.filter(batch_ID=studentbatch_ID):
        subWisePercent={}
        rollCallWeek=Attendance.objects.filter(student_ID=student_ID, subject_ID=subject.id, timestamp__lte=date_end, timestamp__gte=date_start)
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
    date_today=datetime.datetime.now()

    #to iterate all over the active months
    if date_today.date().month >= projparams.SEM1_START_MONTH and date_today.date().month < projparams.SEM2_START_MONTH:
        startMonthPoint = date_today.replace(month=projparams.SEM1_START_MONTH,day=1,hour=0, minute=0)
    else:
        startMonthPoint = date_today.replace(month=projparams.SEM2_START_MONTH,day=1,hour=0, minute=0)

    endMonthPoint = date_today.replace(month = date_today.date().month + 1 ,day=1,hour=0, minute=0)
    studentbatch_ID=Student.batch_ID  #find students batch id
    responseArray=[]

    iteratingMonthStart = startMonthPoint
    iteratingMonthEnd = startMonthPoint.replace()

    while iteratingMonthStart < endMonthPoint:
        month_data = {}
        month_data['start_date']= str(iteratingMonthStart)
        month_data['end_date']= str(iteratingMonthEnd)
        month_data['subjects_data']=[];
        for subject in Subjects.objects.filter(batch_ID=studentbatch_ID):
            subWisePercent={}
            rollCallWeek=Attendance.objects.filter(student_ID=student_ID, subject_ID=subject.id, timestamp__gte=iteratingMonthStart, timestamp__lte=iteratingMonthEnd)
            perc=percentageRoll(rollCallWeek)
            #adding details in dictionary
            subWisePercent['subcode']=Subject.subjectCode
            subWisePercent['subname']=Subject.subjectName
            subWisePercent['Percentage']=perc
            month_data['subjects_data'].append(subWisePercent)

        responseArray.append(month_data)
        iteratingMonthStart=increment_month_start(iteratingMonthStart)
        iteratingMonthEnd = increment_month_end(iteratingMonthEnd)

    response = HttpResponse(json.dumps(responseArray), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@login_required
def date_wise(request):
    #collecting form data
    if ('date' in request.GET) and ('month' in request.GET) and ('year' in request.GET) and request.GET['date'] and request.GET['month'] and request.GET['year']:
        date_form = request.GET['date']
        month_form  = request.GET['month']
        year_form = request.GET['year']

    else:
        return render(request, 'same.html', {'error': True})

    date_today=datetime.datetime.now()
    day_start =  datetime.datetime( year_form, month_form, date_form, 00 , 01 , 00)  #(Year, Month, day, Hour, Minute, second)
    day_end =  datetime.datetime( year_form, month_form, date_form, 23 , 59 , 59)

    studentbatch_ID=Student.batch_ID  #find students batch id
    responseArray=[]
    for subject in Subjects.objects.filter(batch_ID=studentbatch_ID).order_by(subject_name):
        subWisePercent={}
        rollCallWeek=Attendance.objects.filter(student_ID=student_ID, subject_ID=subject.id, updated__lte=day_end, updated__gt=day_start)
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
def date_in_month(request,offset):
    if offset < 0 :
        return render(request, 'error.html', {'error': True})

    date_today=datetime.datetime.now()

    startDayPoint = date_today.replace(day=1,hour=0, minute=0, second=1)
    endDayPoint = increment_month_start(startDayPoint)

    studentbatch_ID=Student.batch_ID  #find students batch id

    responseArray=[]
    iteratingDayStart = startDayPoint
    iteratingDayEnd = startDayPoint.replace(hour=23, minute=59, second=59)
    delta=datetime.timedelta(days=1)
    while iteratingDayStart < endDayPoint:
        date_data ={}
        date_data['_date']= iteratingDayStart.date
        date_data['subjects_data']=[];
        for subject in Subjects.objects.filter(batch_ID=studentbatch_ID):
            subWisePercent={}
            rollCallWeek=Attendance.objects.filter(student_ID=student_ID, subject_ID=subject.id, timestamp__gte=iteratingDayStart, timestamp__lte=iteratingDayEnd)
            perc=percentageRoll(rollCallWeek)
            #adding details in dictionary
            subWisePercent['subcode']=Subject.subjectCode
            subWisePercent['subname']=Subject.subjectName
            subWisePercent['Percentage']=perc
            date_data['subjects_data'].append(subWisePercent)

        responseArray.append(date_data)
        iteratingDayStart=iteratingDayStart+delta
        iteratingDayEnd=iteratingDayEnd+delta

    response = HttpResponse(json.dumps(responseArray), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response



@login_required
def allDaysInMonth(request):
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


