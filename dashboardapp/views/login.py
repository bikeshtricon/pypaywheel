from django.http import HttpResponse
from django.template import RequestContext, loader


def log_in(request):

    #posts = Posts.objects.order_by('-pub_date')[:5]
    
    template = loader.get_template('login.html')
    context = RequestContext(request, {'latest_blog_posts': "posts",})
    return HttpResponse(template.render(context))


