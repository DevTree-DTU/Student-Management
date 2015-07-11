from django.db import models
from login.models import Teacher, Student,Batch
#import subjects

# Create your models here.
class attendance(models.Model):
    studentId = models.ForeignKey(Student,db_index=True)  #indexing is on for studentId
    batchId = models.ForeignKey(Batch,db_index=True)  #indexing is on for batchId
    subjectId= models.ForeignKey(Subject)
    teacherId = models.ForeignKey(Teacher)
    date=models.DateField()
    #time=models.DateField()
    #attendanceWeight=models.BigIntegerField()

     class Meta:
        index_together = [['batchId', 'studentId']]
