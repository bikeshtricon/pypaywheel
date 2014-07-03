from django.http import HttpResponse
from django.template import RequestContext, loader

#for getting user data
from django.contrib.auth.models import User, Group

#for auth and login
from django.contrib.auth import authenticate, login

#for login required decorator
from django.contrib.auth.decorators import login_required, user_passes_test

#for redirect
from django.shortcuts import redirect



from pprint import pprint

from pypaywheel.models import leaveRegister

from pypaywheel.models import leaveType


import logging

# Get an instance of a logger
log = logging.getLogger(__name__)



def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['hr'])

#@login_required(login_url='/login/')
#@user_passes_test(is_in_multiple_groups, login_url='/login/')
def dashboard(request):

    #user = User.objects.create_user('anjnee', 'anjnee@triconinfotech.com', 'password')
    
    # if you want to change other fields.
    #user.last_name = 'sharma'
    #user.save()
    
    #g = Group.objects.get(name='developer') 
    #g.user_set.add(user)

    #login in
    user = authenticate(username='john', password="password")
    


    
    #group = Group(name="developer")
    #group.save()

    #login in hr user
    
    
    #working
    leaveRequests = leaveRegister.objects.filter(status='') .select_related() #leaveType
    
    '''
    for b in bs:
        #log.info(b.leaveType)
        log.info(b.leaveType.status)
        log.info(b.hrId.username)
        log.info(b.uId.username)
        log.info("----------------------")
    '''  
    
    template = loader.get_template('hr/index.html')
     
    context = RequestContext(request, {'leaveRequests': leaveRequests,})
    
    return HttpResponse(template.render(context))


#@login_required(login_url='/login/')
#@user_passes_test(is_in_multiple_groups, login_url='/login/')
def leaveRequestsaction(request, reqId, action):
    
    actions=['accept', 'reject']
    
    leaveRequests = leaveRegister.objects.filter(id=reqId).select_related()
    
    if action in actions and leaveRequests:
        #leaveRegister.objects.filter(id=reqId).update(status=action)
        
        #sendning mail to user
        
        for leaveRequest in leaveRequests:
            leaveRequest.uId.email
            log.info("leaveRequests.uId.email "+leaveRequest.uId.email)
        
    return redirect('/hr')

