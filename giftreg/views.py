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

from django.db.models import Avg, Max, Min, Count

from django.core import serializers

import datetime
import models
import forms


@login_required
def index(request):



#    $query = "SELECT itemid, description, c.category, price, url, rendered, comment, image_filename FROM {$OPT["table_prefix"]}items i LEFT OUTER JOIN {$OPT["table_prefix"]}categories c ON c.categoryid = i.category LEFT OUTER JOIN {$OPT["table_prefix"]}ranks r ON r.ranking = i.ranking WHERE userid = " . $userid . " ORDER BY $sortby";
    itemsIWant = models.Item.objects.filter(User=models.User.objects.get(pk=request.user.id))


#    $query = "SELECT u.userid, u.fullname, u.comment, u.list_stamp, COUNT(i.itemid) AS itemcount " .
#                                "FROM {$OPT["table_prefix"]}shoppers s " .
#                                "INNER JOIN {$OPT["table_prefix"]}users u ON u.userid = s.mayshopfor " .
#                                "LEFT OUTER JOIN {$OPT["table_prefix"]}items i ON u.userid = i.userid " .
#                                "WHERE s.shopper = " . $userid . " " .
#                                    "AND pending = 0 " .
#                                "GROUP BY u.userid, u.fullname, u.list_stamp " .
#                                "ORDER BY u.fullname";
    peopleImShoppingFor = models.Shopper.objects.filter(shopperUser=models.User.objects.get(pk=request.user.id)).filter(pending=False)




#                    /*$query = "SELECT u.userid, u.fullname, s.pending " .
#                                "FROM {$OPT["table_prefix"]}users u " .
#                                "LEFT OUTER JOIN {$OPT["table_prefix"]}shoppers s ON u.userid = s.mayshopfor " .
#                                    "AND s.shopper = " . $userid . " " .
#                                "WHERE u.userid <> " . $userid . " " .
#                                    "AND (s.pending IS NULL OR s.pending = 1) " .
#                                    "AND approved = 1 " .
#                                "ORDER BY u.fullname";*/
#                    $query = "SELECT DISTINCT u.userid, u.fullname, s.pending " .
#                                "FROM {$OPT["table_prefix"]}memberships mymem " .
#                                "INNER JOIN {$OPT["table_prefix"]}memberships others " .
#                                    "ON others.familyid = mymem.familyid AND others.userid <> " . $userid . " " .
#                                "INNER JOIN {$OPT["table_prefix"]}users u " .
#                                    "ON u.userid = others.userid " .
#                                "LEFT OUTER JOIN {$OPT["table_prefix"]}shoppers s " .
#                                    "ON s.mayshopfor = others.userid AND s.shopper = " . $userid . " " .
#                                "WHERE mymem.userid = " . $userid . " " .
#                                    "AND (s.pending IS NULL OR s.pending = 1) " .
#                                    "AND u.approved = 1 " .
#                                "ORDER BY u.fullname";
   
    peopleImNotShoppingFor = User.objects.all()



#$query = "SELECT messageid, u.fullname, message, created " .
#                                "FROM {$OPT["table_prefix"]}messages m " .
#                                "INNER JOIN {$OPT["table_prefix"]}users u ON u.userid = m.sender " .
#                                "WHERE m.recipient = " . $userid . " " .
#                                    "AND m.isread = 0 " .
#                                    "ORDER BY created DESC";
    

    messages = models.Message.objects.filter(recipient=models.User.objects.get(pk=request.user.id))



#                    $query = "SELECT CONCAT(YEAR(CURDATE()),'-',MONTH(eventdate),'-',DAYOFMONTH(eventdate)) AS DateThisYear, " .
#                                "TO_DAYS(CONCAT(YEAR(CURDATE()),'-',MONTH(eventdate),'-',DAYOFMONTH(eventdate))) AS ToDaysDateThisYear, " .
#                                "CONCAT(YEAR(CURDATE()) + 1,'-',MONTH(eventdate),'-',DAYOFMONTH(eventdate)) AS DateNextYear, " .
#                                "TO_DAYS(CONCAT(YEAR(CURDATE()) + 1,'-',MONTH(eventdate),'-',DAYOFMONTH(eventdate))) AS ToDaysDateNextYear, " .
#                                "TO_DAYS(CURDATE()) AS ToDaysToday, " .
#                                "TO_DAYS(eventdate) AS ToDaysEventDate, " .
#                                "e.userid, u.fullname, description, eventdate, recurring, s.pending " .
#                            "FROM {$OPT["table_prefix"]}events e " .
#                            "LEFT OUTER JOIN {$OPT["table_prefix"]}users u ON u.userid = e.userid " .
#                            "LEFT OUTER JOIN {$OPT["table_prefix"]}shoppers s ON s.mayshopfor = e.userid AND s.shopper = $userid ";
#                    if ($OPT["show_own_events"])
#                        $query .= "WHERE (pending = 0 OR pending IS NULL)";
#                    else
#                        $query .= "WHERE (e.userid <> $userid OR e.userid IS NULL) AND (pending = 0 OR pending IS NULL)";
#                    $query .= "ORDER BY u.fullname";

    event_threshold_int_days  = 90
    #events = models.Event.objects.filter(eventdate__gt = datetime.date.today() + datetime.timedelta(days=+event_threshold_int_days))
    events = models.Event.objects.all()
 



#$query = "SELECT u.userid, u.fullname " .
#                                    "FROM {$OPT["table_prefix"]}shoppers s " .
#                                    "INNER JOIN {$OPT["table_prefix"]}users u ON u.userid = s.shopper " .
#                                    "WHERE s.mayshopfor = " . $userid . " " .
#                                        "AND s.pending = 1 " .
#                                    "ORDER BY u.fullname";
#    
    peopleWhoWantToShopForMe = User.objects.all()
    
    
#    $query = "SELECT userid, fullname, email, approved, initialfamilyid, familyname " .
#                                    "FROM {$OPT["table_prefix"]}users u " .
#                                    "LEFT OUTER JOIN {$OPT["table_prefix"]}families f ON f.familyid = u.initialfamilyid " .
#                                    "WHERE approved = 0 " . 
#                                    "ORDER BY fullname";
    peopleWaitingApproval = User.objects.all()
    
    numItems = 0
    for x in itemsIWant:
        numItems = numItems + x.quantity
    
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
#    ShoppingListFormSet = modelformset_factory(models.Item)
#    if request.method == 'POST':
#        formset = ShoppingListFormSet(request.POST)
#        formset.save()
#    else:
#        formset = ShoppingListFormSet()
#    items = models.Item.objects.all()

    #items = models.Alloc.objects.filter(user__id_exact=request.user.id).
    items = models.Alloc.objects.all().select_related()
    
#$query = "SELECT description, source, price, i.comment, a.quantity, a.quantity * i.price AS total, rendered, fullname " .
#            "FROM {$OPT["table_prefix"]}items i " .
#            "INNER JOIN {$OPT["table_prefix"]}users u ON u.userid = i.userid " .
#            "INNER JOIN {$OPT["table_prefix"]}ranks r ON r.ranking = i.ranking " .
#            "INNER JOIN {$OPT["table_prefix"]}allocs a ON a.userid = $userid AND a.itemid = i.itemid AND bought = 0 " .
#            "ORDER BY $sortby";    
    
    totalItems = items.aggregate('quantity')
    totalPrice = items.aggregate('price')
    
    return render_to_response('shoplist.html', 
                              {
                               'items' : items,
                               'totalItems': totalItems,
                               'totalPrice': totalPrice,
                               },
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


################################# Events ####################################

@login_required
@permission_required('giftReg.event')
def event(request):
#    EventFormSet = modelformset_factory(models.Event)
#    if request.method == 'POST':
#        formset = EventFormSet(request.POST)
#        formset.save()
#    else:
#        formset = EventFormSet()

    # we need to create
    # system events --- for everyone (christmas, actuall holidays
    # family events --- specific to a family
    events = models.Event.objects.all()
    return render_to_response('event.html', {'events' : events, },
                                             context_instance=RequestContext(request))



#@login_required
@permission_required('giftReg.event')
def eventAdd(request):
    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        if form.is_valid():
            new_family = form.save()
            return redirect('/giftReg/event')
    else:
        form = forms.EventForm()
    return render_to_response('eventEdit.html', {'form' : form },
                                             context_instance=RequestContext(request))

#@login_required
@permission_required('giftReg.event')
def eventEdit(request, eventid):
    if request.method == 'POST':
        rank = models.Event.objects.get(pk=eventid)
        form = forms.EventForm(request.POST, instance=rank)
        if form.is_valid():
            new_family = form.save()
            return redirect('/giftReg/event')
    else:
        rank = models.Family.objects.get(pk=eventid)
        form = forms.EventForm(instance=rank)
    return render_to_response('eventEdit.html', {'form' : form },
                                             context_instance=RequestContext(request))
    
#@login_required
@permission_required('giftReg.event')
def eventDelete(request, eventid):
    event = models.Event.objects.filter(id=eventid)
    event.delete()
    return redirect('/giftReg/event')
    











###################### Families #################################################################

@login_required
@permission_required('giftReg.family')
def families(request):
#    FamilyFormSet = modelformset_factory(models.Family)
#    if request.method == 'POST':
#        formset = FamilyFormSet(request.POST)
#        formset.save()
#    else:
#        formset = FamilyFormSet()
    families = models.Family.objects.order_by('FamilyName').annotate(FamilyMemberCount=Count('FamilyMember'))
    return render_to_response('families.html', {'families' : families, },
                                             context_instance=RequestContext(request))
    
    
    

#@login_required
@permission_required('giftReg.family')
def familyAdd(request):
    if request.method == 'POST':
        form = forms.FamilyForm(request.POST)
        if form.is_valid():
            new_family = form.save()
            return redirect('/giftReg/families')
    else:
        form = forms.FamilyForm()
    return render_to_response('familyEdit.html', {'form' : form },
                                             context_instance=RequestContext(request))

#@login_required
@permission_required('giftReg.family')
def familyEdit(request, familyid):
    if request.method == 'POST':
        rank = models.Family.objects.get(pk=familyid)
        form = forms.FamilyForm(request.POST, instance=rank)
        if form.is_valid():
            new_family = form.save()
            return redirect('/giftReg/families')
    else:
        rank = models.Family.objects.get(pk=familyid)
        form = forms.FamilyForm(instance=rank)
    return render_to_response('familyEdit.html', {'form' : form },
                                             context_instance=RequestContext(request))
    
#@login_required
@permission_required('giftReg.family')
def familyDelete(request, familyid):
    family = models.Family.objects.filter(id=familyid)
    family.delete()
    return redirect('/giftReg/families')
    