from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from pypaywheel.models import leaveRegister
from pypaywheel.models import leaveType
from django.core.mail import send_mail
import urllib
import http.client
from base64 import b64encode
import logging
logger = logging.getLogger(__name__)


def dashboard(request):
    
    username = request.user.username
    leaveTypes = leaveType.objects.all()
    current_user = request.user
    
    uId = current_user.id
    '''
    conn = http.client.HTTPConnection("pay.in")
    userAndPass = b64encode(b"tricon:tricon8").decode("ascii")
    headers = { 'Authorization' : 'Basic %s' %  userAndPass }
    conn.request("GET", "/apis/cacheRefresh",headers=headers)
    r1 = conn.getresponse()
    '''  
    url = "http://pay.in/apis/cacheRefresh"
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, 'tricon', 'tricon8')
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        
    opener = urllib.request.build_opener(handler)
    
    
    try:
        req = urllib.request.Request(url)
        response = opener.open(req)
           
    except urllib.request.HTTPError as e:
        if e.code ==  401or e.code == 403:
            logger.debug('not authorized..........')
            return HttpResponse("there is some error  401 403")
        elif e.code == 404:
            logger.debug('not found.............')
            return HttpResponse("there is some error 404")
        else:
            logger.debug('Error: %s' % e.code)
            logger.debug( e)
            logger.debug('unknown error:....cache..... ')
            return HttpResponse("unknown error 500")
    else:
        binaryResponse = response.read()
        
        logger.debug("------------------start-1--------------------")
        logger.debug("responseXML  = %s" %binaryResponse)
        logger.debug("------------------end-1------------------")   
            
            
    
    data = "anjnee.k.sharma"
    #data['email'] = "anjnee@triconinfotech.com" 
    
    binary_data = data.encode('utf-8')  
    Url = "http://pay.in/createUser"
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, Url, 'tricon', 'tricon8')
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)
    
    
    try:    
            
            req = urllib.request.Request(Url,binary_data,method='POST')
            req.add_header('Content-Type', 'text/plain; charset=utf-8')
            req.add_header('Content-Length', len(binary_data))
            logger.debug(req)
            response = opener.open(req)
            logger.debug("-INSIDE TRY-")
           
    except urllib.request.HTTPError as e:
            if e.code ==  401or e.code == 403:
                logger.debug('not authorized..........')
                return HttpResponse('not authorized..........')
            elif e.code == 404:
                logger.debug('not found.............')
                return HttpResponse('not found.............')
            else:
                logger.debug('Error: %s' % e.code)
                logger.debug('unknown error:...for create user...... ')
                return HttpResponse('unknown error:...for create user...... ')
    else:
            binaryResponse = response.read()
                
            # Convert the response binary xml into String xml
            responseXML = binaryResponse.decode('utf-8')
            
            logger.debug("------------------start-2--------------------")
            logger.debug("responseXML for create user = %s" %responseXML)
            logger.debug("------------------end-2------------------")   
            
                          
    
    
    
    
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
    
    #added new line for testing
