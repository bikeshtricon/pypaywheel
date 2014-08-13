from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from pypaywheel.models import leaveRegister
from pypaywheel.models import leaveType
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)


def dashboard(request):
    
    username = request.user.username
    leaveTypes = leaveType.objects.all()
    current_user = request.user
    
    uId = current_user.id
    
    logger.debug("uId =   %s"%uId)
    
    if 'from' in request.POST:
        leave_from = request.POST['from']
        leave_to = request.POST['to']
        reason = request.POST['reason']

        
        selectedLeaveType = int(request.POST['leavetype'])
        
        logger.debug("selectedLeaveType =   %s"%selectedLeaveType)
        ltype = leaveType.objects.get(pk=selectedLeaveType)
        hrId = User.objects.get(pk=1)
        
        '''data base insertion'''
        ob = leaveRegister(uId = request.user,leaveType = ltype, leaveFrom = leave_from, leaveTo = leave_to,  reason = reason,hrId = hrId, status = "")
        ob.save()
        subject = 'leave'
        message = 'your leave have been approved'
        frm = 'anjneesharma@gmail.com'
        try:
            send_mail(subject, message, frm, ['anjneekumar17@gmail.com'], fail_silently=False)
        except Exception as e:
            return HttpResponse(e)
        else:
            return HttpResponse("Email sent successfully")
            
        
   
    template = loader.get_template('dashboardapp/dashboard.html')
    context = RequestContext(request, {'username': username,'leavetype':leaveTypes})
    return HttpResponse(template.render(context))
    
    //added new line for testing
