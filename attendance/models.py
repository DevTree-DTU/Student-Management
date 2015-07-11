from django.db import models
from login.models import Teacher, Student,Batch
#import subjects

# Create your models here.
class attendance(models.Model):
    studentId = models.ForeignKey(Student)
    batchId = models.ForeignKey(Batch)
    subjectId= models.ForeignKey(Subject)
    teacherId = models.ForeignKey(Teacher)
    #time=models.DateField()
    #attendanceWeight=models.BigIntegerField()
