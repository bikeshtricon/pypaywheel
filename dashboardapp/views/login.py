from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
import logging
logger = logging.getLogger(__name__)


def log_in(request):

    #posts = Posts.objects.order_by('-pub_date')[:5]
    
    
    #data = template(request)
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)
        logger.debug("user = %s"%user)
        if user is not None:
            login(request, user)
            #logger.debug("Group =%s"%user.groups.values_list('name',flat=True))
            #group = user.groups.values_list('name',flat=True)
            
            if user.groups.filter(name__in=['hr']):
                logger.debug("ye user is hr")
                return HttpResponseRedirect("/hr")
                
            elif user.groups.filter(name__in=['developer']):
                logger.debug("ya i am a developer")
                
                
                
            else:  
                logger.debug("not a developer ans hr")
    
    
    template = loader.get_template('login.html')
    context = RequestContext(request, {'latest_blog_posts': "posts",})
    return HttpResponse(template.render(context))


