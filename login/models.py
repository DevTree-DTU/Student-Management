from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    address = moels.CharField(max_length=100)
    department = models.CharField(max_length=20)
    roomNo = models.CharField(max_length=10)
    designation = models.CharField(max_length=20)
    expertise = models.CharField(max_length=20)
    phoneNo = models.BigIntegerField()
    email = models.EmailField()
    dateOfJoining = models.DateField()
    isHOD = models.BooleanField()

class Student(models.Model):
    name = models.CharField(max_length=50)
    address = moels.CharField(max_length=100)
    phoneNo = models.BigIntegerField()
    email = models.EmailField()
    fathersName = models.CharField(max_length=50)
    DOB = models.DateField()
    isCR = models.BooleanField()
    #password
    studentID = models.CharField(max_length=50)
    batchID = models.CharField(max_length=50)
    branch = models.CharField(max_length=30)
    admissionYear = models.CharField(max_length=10)

class Assignment(models.Model):
    url = models.URLField(max_length=50)
    batchID = models.CharField(max_length=50)
    dueDate = models.DateField()
    teacherID = models.CharField(max_length=30)
    date = models.CharField(max_length=30)

class TimeTable(models.Model):
    batchID = models.CharField(max_length=50)
    teacherID = models.CharField(max_length=30)
    start = models.TimeField()
    end = models.TimeField()
    day = models.CharField(max_length=10)
    subjectID = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)

class Batch(models.Model):
    batchID = models.CharField(max_length=50)
    year = models.CharField(max_length=5)
    studentCount = models.BigIntegerField()
    subjectCount = models.BigIntegerField()
    cr = models.CharField(max_length=30)
    #How to handle Subject Names
