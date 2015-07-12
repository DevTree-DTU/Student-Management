from django.shortcuts import render
import datetime
def percentageCalc(listOfRollCalls):
    totalCalls=0
    presentCalls=0
    recentPresentCalls=0  #stores last complete months attendance.
    recentTotalCalls=0

    previousMonth=datetime.date.today().month - 1

    for rollCall in listOfRollCalls
        totalCalls+=rollCall.attendanceWeight
        presentCalls+=rollCall.presentPoints
        if rollCall.date.month==previousMonth:
            recentTotalCalls+=rollCall.attendanceWeight
            recentPresentCalls+=rollCall.presentPoints
    return (recentPresentCalls*100.0/recentTotalCalls,presentCalls*100.0/totalCalls)


def studentPercentage(request):
    #student_id=
    allRollCalls=attendance.objects.filter(studentId=student_id)
    percentages=percentageCalc(allRollCalls)
    return {'monthlyPercentage':percentages[0],'TotalPercentage':percentages[1] }

def rollCallForBatch(request)
    #selectBatch
    #loadstudents
    #send student names
    #get present/absent/attendance
    #save the records

def editAttendanceForBatch()
    #selectBatch
    #selectSubject
    #fetch all roll calls
    #send the json
