#Currently we have only one of the below models set as the default Auth model. In the next build, probably a middleware class will
#added 2

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
class TeacherManager(BaseUserManager):
    def create_user(self, tPassword, tUsername, tName, tAddress, tDepartment, tRoomNo, tDesignation, tExpertise, tPhoneNo, tEmail, tDateOfJoining, tIsHOD, tIsAdmin, tIsSuperuser):
        if not tUsername:
            raise ValueError('Teacher Username Required')
        teacher = self.model(username=tUsername, name = tName, address = tAddress, department = tDepartment,roomNo = tRoomNo, designation = tDesignation,
        expertise = tExpertise, phoneNo = tPhoneNo, email = tEmail, dateOfJoining = tDateOfJoining, isHOD = tIsHOD)
        teacher.set_password(tPassword)
        teacher.is_active = True
        if(tIsAdmin == True):
            t.is_admin = True
        teacher.save(self._db)
        return teacher
    def create_superuser(self, tPassword, tUsername, tName, tAddress, tDepartment, tRoomNo, tDesignation, tExpertise, tPhoneNo, tEmail, tDateOfJoining, tIsHOD):
        if not tUsername:
            raise ValueError('Username Required')
        teacher = self.model(username=tUsername, name = tName, address = tAddress, department = tDepartment,roomNo = tRoomNo, designation = tDesignation,
        expertise = tExpertise, phoneNo = tPhoneNo, email = tEmail, dateOfJoining = tDateOfJoining, isHOD = tIsHOD)
        teacher.set_password(tPassword)
        teacher.is_admin = True
        teacher.is_active = True
        teacher.save(self._db)
        return teacher

class StudentManager(BaseUserManager):
    def create_user(self, sUsername, sPassword, sName, sAddress, sPhoneNo, sEmail, sFathersName, sDOB, sIsCR, sStudentID, sBatchID, sBranch, sAdmissionYear):
        if not sUsername:
            raise ValueError('Student Username Required')
        student = self.model(username=sUsername,name=sName,address=sAddress,phoneNo=sPhoneNo,email=sEmail,fathersName=sFathersName,DOB=sDOB,isCR=sIsCR,studentID=sStudentID,batchID=sBatchID,branch=sBranch,admissionYear=sAdmissionYear)
        student.set_password(self.cleaned_data[sPassword])
        student.is_active=True
        student.save(self._db)
        return student

class AssignmentManager(BaseUserManager):
    def create_user(aUrl,aBatchID,aDueDate,aTeacherID,aDate):
        if not aUrl:
            raise ValueError('Invalid Assignment')

        assignment = self.model(url=aUrl,batchID=aBatchID,dueDate=aDueDate,teacherID=aTeacherID,date=aDate)
        assignment.save(self._db)
        return student

class TimeTableManager(BaseUserManager):
    def create_user(ttBatchID,ttTeacherID,ttStart,ttEnd,ttDay,ttSubjectID,ttVenue):
        if not ttSubjectID:
            raise ValueError('No Subject Assigned')

        timetable = self.model(batchID=ttBatchID,teacherID=ttTeacherID,start=ttStart,end=ttEnd,day=ttDay,subjectID=ttSubjectID,venue=ttVenue)
        timetable.save(self._db)
        return timetable

class BatchManager(BaseUserManager):
    def create_user(bBatchID,bYear,bStudentCount,bSubjectCount,bCr):
        if not ttBatchID:
            raise ValueError('No Batch ID')

        batch = self.model(batchID=bBatchID,year=bYear,studentCount=bStudentCount,subjectCount=bSubjectCount,cr=bCr)
        batch.save(self._db)
        return batch

class Teacher(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    department = models.CharField(max_length=20)
    roomNo = models.CharField(max_length=10)
    designation = models.CharField(max_length=20)
    expertise = models.CharField(max_length=20)
    phoneNo = models.BigIntegerField()
    email = models.EmailField()
    dateOfJoining = models.DateField()
    isHOD = models.BooleanField()
    is_admin = models.BooleanField(default=False)
    objects=TeacherManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['name','phoneNo','email']
    def get_full_name(self):
        return self.email
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

class Student(AbstractBaseUser):
    username = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    phoneNo = models.BigIntegerField()
    email = models.EmailField(unique=True, null=True)
    fathersName = models.CharField(max_length=50, null=True)
    DOB = models.DateField(null=True)
    isCR = models.NullBooleanField()
    is_admin = models.BooleanField(default=False)
    studentID = models.CharField(max_length=50, null=True)
    batchID = models.CharField(max_length=50, null=True)
    branch = models.CharField(max_length=30, null=True)
    admissionYear = models.CharField(max_length=10, null=True)
    objects=StudentManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['name','phoneNo']
    def get_full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return self.email

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin

class Assignment(AbstractBaseUser):
    url = models.URLField(max_length=50,unique=True)
    batchID = models.CharField(max_length=50)
    dueDate = models.DateField()
    teacherID = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    objects=AssignmentManager()
    USERNAME_FIELD='url'
    REQUIRED_FIELDS=['batchID','dueDate','teacherID']
    def get_full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return self.email

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.url

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin


class TimeTable(AbstractBaseUser):
    batchID = models.CharField(max_length=50,unique=True)
    #This shouldn't be unique since the timetable has multiple entries for each batch
    #Soltuion needed for this. Reason being each AbstractBaseUser needs a unique values column.
    teacherID = models.CharField(max_length=30)
    start = models.TimeField()
    end = models.TimeField()
    day = models.CharField(max_length=10)
    subjectID = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    objects=TimeTableManager()
    USERNAME_FIELD='batchID'
    REQUIRED_FIELDS=['start','end','day','subjectID','teacherID']
    def get_full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return self.email

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.batchID

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin


class Batch(AbstractBaseUser):
    batchID = models.CharField(max_length=50,unique=True)
    year = models.CharField(max_length=5)
    studentCount = models.BigIntegerField()
    subjectCount = models.BigIntegerField()
    cr = models.CharField(max_length=30)
    objects=BatchManager()
    USERNAME_FIELD='batchID'
    REQUIRED_FIELDS=['year']
    def get_full_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return self.email

    def get_short_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.email

    def __unicode__(self):
        return self.batchID
    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin
    #How to handle Subject Names

class RequestMiddleware(object):
    def process_request(self,request):
        agent = request.POST.get('agent', 'Teacher')
        if agent == 'Student':
            settings.AUTH_USER_MODEL='login.Student'
        elif agent == 'Teacher':
            settings.AUTH_USER_MODEL='login.Teacher'
        elif agent == 'Assignment':
            settings.AUTH_USER_MODEL='login.Assignemnt'
        elif agent == 'TimeTable':
            settings.AUTH_USER_MODEL='login.TimeTable'
        elif agent == 'Batch':
            settings.AUTH_USER_MODEL='login.Batch'
