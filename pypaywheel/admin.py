from django.contrib import admin

from pypaywheel.models import leaveRegister 

from pypaywheel.models import leaveType

admin.site.register(leaveType)

admin.site.register(leaveRegister)
