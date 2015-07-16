from django.db import models
from login.models import Teacher, Student,Batch
#import subjects

# Create your models here.
class Attendance(models.Model):
    studentID = models.ForeignKey(Student,db_index=True)  #indexing is on for studentId
    batchID = models.ForeignKey()  #indexing is on for batchId
    subjectID= models.ForeignKey(Subject)
    teacherID = models.ForeignKey(Teacher)
    date=models.DateField()
    presentPoints=models.IntegerField()
    attendanceWeight=models.IntegerField()


     class Meta:
        index_together = [['batchId', 'studentId']]  #useful for editing the attendance
