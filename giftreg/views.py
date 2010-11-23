# Create your views here.
#from django.template.loader import get_template
#from django.template import Template, Context
#from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required

from django.core import serializers
import models
import forms


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
    
    if request.method == 'POST':
        form = forms.ItemAddModelForm(request.POST)
        #form.User = request.user.id
        if form.is_valid():
            inst = form.save(commit=False)
            inst.User = models.User.objects.get(pk=request.user.id)
            inst.save()
            #            cd = form.cleaned_data
#            send_mail(
#                cd['subject'],
#                cd['message'],
#                cd.get('email', 'noreply@example.com'),
#                ['siteowner@example.com'],
#            )

            return redirect('/')
    else:
        form = forms.ItemAddModelForm()
    return render_to_response('itemAdd.html', {'form': form}, context_instance=RequestContext(request))


#@login_required
@permission_required('giftReg.category')
def categories(request):
    CategoriesFormSet = modelformset_factory(models.Category)
    if request.method == 'POST':
        formset = CategoriesFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('giftReg/categories')
    else:
        formset = CategoriesFormSet()
    categories = models.Category.objects.all()
    return render_to_response('categories.html', {'categories' : categories, 'formset' : formset },
                              context_instance=RequestContext(request))


#from django.utils import simplejson

#@login_required
@permission_required('giftReg.rank')
def ranks(request):
    #rankData = serializers.serialize('json', models.Rank.objects.all())
    #simplejson.dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, encoding, default)
    RankFormSet = modelformset_factory(models.Rank)
    if request.method == 'POST':
        formset = RankFormSet(request.POST)
        formset.save()
    else:
        formset = RankFormSet()
    ranks = models.Rank.objects.order_by('rankorder')
    return render_to_response('ranks.html', {'ranks' : ranks,
                                             'formset' : formset },
                                             context_instance=RequestContext(request))





#@login_required
@permission_required('giftReg.rank')
def rankAdd(request):
    if request.method == 'POST':
        form = forms.RankForm(request.POST)
        if form.is_valid():
            new_rank = form.save()
            return redirect('/giftReg/ranks')
    else:
        form = forms.RankForm()
    return render_to_response('rankEdit.html', {'form' : form },
                                             context_instance=RequestContext(request))

#@login_required
@permission_required('giftReg.rank')
def rankEdit(request, rankid):
    if request.method == 'POST':
        rank = models.Rank.objects.get(pk=rankid)
        form = forms.RankForm(request.POST, instance=rank)
        if form.is_valid():
            new_rank = form.save()
            return redirect('/giftReg/ranks')
    else:
        rank = models.Rank.objects.get(pk=rankid)
        form = forms.RankForm(instance=rank)
    return render_to_response('rankEdit.html', {'form' : form },
                                             context_instance=RequestContext(request))
    
#@login_required
@permission_required('giftReg.rank')
def rankDelete(request, rankid):
    rank = models.Rank.objects.filter(rankid=rankid)
    rank.delete()
    return redirect('/giftReg/ranks')

#@login_required
@permission_required('giftReg.rank')
def rankPromote(request, rankid):
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


#@login_required
@permission_required('giftReg.rank')
def rankDemote(request, rankid):
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












@login_required
def shoppinglist(request):
    ShoppingListFormSet = modelformset_factory(models.Item)
    if request.method == 'POST':
        formset = ShoppingListFormSet(request.POST)
        formset.save()
    else:
        formset = ShoppingListFormSet()
    items = models.Item.objects.all()
    return render_to_response('shoplist.html', {'items' : items,
                                             'formset' : formset },
                                             context_instance=RequestContext(request))
        
@login_required
def mylist(request, sortheader):
    if not sortheader:
        itemsIWant = models.Item.objects.filter(User=models.User.objects.get(pk=request.user.id))
    else:
        itemsIWant = models.Item.objects.filter(User=models.User.objects.get(pk=request.user.id)).order_by(sortheader)
    
    numItems = 0
    totalamount = 0;
#    y, m = 2010, 10 
#    clients = [] 
#    for c in Client.objects.all():
#        clients.append({'client':c, 'purchases':c.get_purchases_month(y, m)}
    for x in itemsIWant:
        numItems = numItems + x.quantity
        x.total = x.price * x.quantity
        totalamount = totalamount + x.total
    return render_to_response('mylist.html', {
                                              'numItems': numItems,
                                              'totalamount': totalamount,
                                              'CurrentUser' : request.user,
                                              'items' : itemsIWant,
                                             },
                                             context_instance=RequestContext(request))

@login_required
def event(request):
    EventFormSet = modelformset_factory(models.Event)
    if request.method == 'POST':
        formset = EventFormSet(request.POST)
        formset.save()
    else:
        formset = EventFormSet()
    events = models.Event.objects.all()
    return render_to_response('event.html', {'events' : events,
                                             'formset' : formset },
                                             context_instance=RequestContext(request))
        
@login_required
def families(request):
    FamilyFormSet = modelformset_factory(models.Family)
    if request.method == 'POST':
        formset = FamilyFormSet(request.POST)
        formset.save()
    else:
        formset = FamilyFormSet()
    families = models.Family.objects.all()
    return render_to_response('families.html', {'families' : families,
                                             'formset' : formset },
                                             context_instance=RequestContext(request))


