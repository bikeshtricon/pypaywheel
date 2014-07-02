from django.http import HttpResponse
from django.template import RequestContext, loader

#for getting user data
from django.contrib.auth.models import User, Group

#for auth and login
from django.contrib.auth import authenticate, login

#for login required decorator
from django.contrib.auth.decorators import login_required, user_passes_test



def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['hr'])

#@login_required(login_url='/login/')
#@user_passes_test(is_in_multiple_groups, login_url='/login/')
def dashboard(request):

    #group = Group(name="developer")
    #group.save()

    #login in hr user
    
    user = authenticate(username='john', password="password")
    

    id= user.id
    
    template = loader.get_template('hr/index.html')
     
    context = RequestContext(request, {'latest_blog_posts': id,})
    
    return HttpResponse(template.render(context))


