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

#for email
from django.core.mail import send_mail

#email from email templet

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


#importing our module
from pypaywheel.models import leaveRegister

from pypaywheel.models import leaveType

#importing login
import logging
log = logging.getLogger(__name__)



def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['hr'])


@login_required(login_url='/dashboardapp/')
@user_passes_test(is_in_multiple_groups, login_url='/dashboardapp/')
def dashboard(request):

    leaveRequests = leaveRegister.objects.filter(status='') .select_related() #leaveType
    
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
            
            #send ing plain text email
            #send_mail('Leave approved', 'Hi '+leaveRequest.uId.first_name+" "+leaveRequest.uId.last_name+" Your leave approved by "+request.user.first_name+" "+request.user.last_name, 'admin@myfriendsgroup.com',[leaveRequest.uId.email], fail_silently=False)

            #email from email templet
            
            plaintext = get_template('email/leaveapproved.txt')
            htmly     = get_template('email/leaveapproved.html')
            
            d = Context({ 'username': leaveRequest.uId.first_name+" "+leaveRequest.uId.last_name, 'action': action })
            
            subject, from_email, to = 'Leave approved', 'admin@myfriendsgroup.com', leaveRequest.uId.email
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        
    return redirect('/hr')

