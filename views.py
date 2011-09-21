# Create your views here.
#from django.template.loader import get_template
#from django.template import Template, Context
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.contrib.auth.decorators import login_required

#import datetime

def index(request):
    #t = Template("index.html")
    #html = t.render(Context({'currentdate':now}))
    #return HttpResponse(html)
    #current_date = datetime.datetime.now()
    #return render_to_response('start.html', locals())
    if request.user.is_authenticated():
        return HttpResponseRedirect('/giftReg/')
    else:
        return render_to_response('start.html', locals())
