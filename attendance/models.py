from django.db import models
from login.models import Teacher, Student,Batch
#import subjects

# Create your models here.
class Attendance(models.Model):
    student_ID = models.ForeignKey(Student,db_index=True)  #indexing is on for studentId
    batch_ID = models.ForeignKey()  #indexing is on for batchId
    subject_ID= models.ForeignKey(Subject)
    teacher_ID = models.ForeignKey(Teacher)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)  #system set, automatically one time,no manual changes allowd
	updated=models.DateTimeField(auto_now_add=False ,auto_now=True)  #system set, automatically updates eac time, no manual changes allowd
    present_points=models.IntegerField()
    weight=models.IntegerField()    #weightage of the attendance roll calll


     class Meta:
        index_together = [['batchId', 'studentId']]  #useful for speeding the editing of attendance
