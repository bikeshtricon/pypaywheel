from django.db import models
'''
from django.contrib.auth.models import User

class leaveType(models.Model):
    type = models.CharField(max_length=200)
    status = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.type

class leaveRegister(models.Model):
    uId = models.ForeignKey(User, related_name = 'leave_appyed_by' )
    leaveType = models.ForeignKey(leaveType)
    leaveFrom = models.DateField()
    leaveTo = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=200)
    hrId =models.ForeignKey(User, related_name = 'leave_approved_by' )
    
'''
