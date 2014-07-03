from django.http import HttpResponse
from django.template import RequestContext, loader
import logging
logger = logging.getLogger(__name__)


def log_in(request):

    #posts = Posts.objects.order_by('-pub_date')[:5]
    
    template = loader.get_template('login.html')
    #data = template(request)
    if 'username' in request.POST:
        logger.error(request.POST['username'])
    #logger.info(data)
    
    
    context = RequestContext(request, {'latest_blog_posts': "posts",})
    return HttpResponse(template.render(context))


