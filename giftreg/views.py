# Create your views here.
#from django.template.loader import get_template
#from django.template import Template, Context
#from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.template import RequestContext

from django.core import serializers


import models

@login_required
def index(request):
    #t = Template("index.html")
    #html = t.render(Context({'currentdate':now}))
    #return HttpResponse(html)
    
    #full_name = request.user.get_full_name()
    messages = models.Message.objects.all()
    itemsIWant = models.Item.objects.all()
    peopleImShoppingFor = User.objects.all()
    peopleImNotShoppingFor = User.objects.all()
    event_threshold_int_days  = 90
    events = models.Event.objects.all()
    peopleWhoWantToShopForMe = User.objects.all()
    peopleWaitingApproval = User.objects.all()
    
    return render_to_response('index.html', {'messages' : messages, 
                                             'items' : itemsIWant, 
                                             'peopleImShoppingFor' :peopleImShoppingFor,
                                             'peopleImNotShoppingFor' : peopleImNotShoppingFor,
                                             'event_threshold_int_days' :event_threshold_int_days,
                                             'events' : events,
                                             'peopleWhoWantToShopForMe' : peopleWhoWantToShopForMe,
                                             'peopleWaitingApproval' : peopleWaitingApproval },
                                             context_instance=RequestContext(request))



@login_required
def itemAdd(request):
     
    #full_name = request.user.get_full_name()
    messages = models.Message.objects.all()
    itemsIWant = models.Item.objects.all()
    peopleImShoppingFor = User.objects.all()
    peopleImNotShoppingFor = User.objects.all()
    event_threshold_int_days  = 90
    events = models.Event.objects.all()
    peopleWhoWantToShopForMe = User.objects.all()
    peopleWaitingApproval = User.objects.all()
    
    return render_to_response('itemAdd.html', {'messages' : messages, 
                                             'items' : itemsIWant, 
                                             'peopleImShoppingFor' :peopleImShoppingFor,
                                             'peopleImNotShoppingFor' : peopleImNotShoppingFor,
                                             'event_threshold_int_days' :event_threshold_int_days,
                                             'events' : events,
                                             'peopleWhoWantToShopForMe' : peopleWhoWantToShopForMe,
                                             'peopleWaitingApproval' : peopleWaitingApproval },
                                             context_instance=RequestContext(request))











@login_required
def categories(request):
    CategoriesFormSet = modelformset_factory(models.Category)
    if request.method == 'POST':
        formset = CategoriesFormSet(request.POST)
        formset.save()
    else:
        formset = CategoriesFormSet()
    categories = models.Category.objects.all()
    return render_to_response('categories.html', {'categories' : categories, 'formset' : formset },
                              context_instance=RequestContext(request))


#from django.utils import simplejson

@login_required
def ranks(request):

    rankData = serializers.serialize('json', models.Rank.objects.all())

#simplejson.dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, encoding, default)
    
    
    RankFormSet = modelformset_factory(models.Rank)
    if request.method == 'POST':
        formset = RankFormSet(request.POST)
        formset.save()
    else:
        formset = RankFormSet()
    ranks = models.Rank.objects.all()
    return render_to_response('ranks.html', {'rankData' : rankData ,
                                             'ranks' : ranks,
                                             'formset' : formset },
                                             context_instance=RequestContext(request))



