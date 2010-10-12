# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
#from django.contrib.auth import authenticate
from django.contrib.auth.models import User
#from django import forms





#class DjangoContentType(models.Model):
#    id = models.IntegerField(primary_key=True)
#    name = models.CharField(max_length=300)
#    # app_label = models.CharField(unique=True, max_length=300)
#    app_label = models.CharField(unique=True, max_length=255)
#    # model = models.CharField(unique=True, max_length=300)
#    model = models.CharField(unique=True, max_length=255)
#    class Meta:
#        db_table = u'django_content_type'
#
#class DjangoSession(models.Model):
#    session_key = models.CharField(max_length=120, primary_key=True)
#    session_data = models.TextField()
#    expire_date = models.DateTimeField()
#    class Meta:
#        db_table = u'django_session'
#
#class DjangoSite(models.Model):
#    id = models.IntegerField(primary_key=True)
#    domain = models.CharField(max_length=300)
#    name = models.CharField(max_length=150)
#    class Meta:
#        db_table = u'django_site'






class Category(models.Model):
    #categoryid = models.IntegerField(primary_key=True)
    #categoryid = models.IntegerField()
    CategoryName = models.CharField(max_length=150, blank=True)
#    class Meta:
#        db_table = u'Category'

class Event(models.Model):
    #eventid = models.IntegerField(primary_key=True)
    #userid = models.IntegerField(null=True, blank=True)
    User = models.ForeignKey(User)
    description = models.CharField(max_length=300)
    eventdate = models.DateField()
    recurring = models.IntegerField()
#    class Meta:
#        db_table = u'Event'

class Family(models.Model):
    #familyid = models.IntegerField(primary_key=True)
    FamilyName = models.CharField(max_length=765)
    FamilyMember = models.ManyToManyField(User)
#    class Meta:
#        db_table = u'Family'


class Rank(models.Model):
    #ranking = models.IntegerField(primary_key=True)
    ranking = models.IntegerField()
    title = models.CharField(max_length=150)
    rendered = models.CharField(max_length=765)
    rankorder = models.IntegerField()
#    class Meta:
#        db_table = u'Rank'


class Item(models.Model):
    #itemid = models.IntegerField(primary_key=True)
    #userid = models.IntegerField()
    User = models.ForeignKey(User)
    description = models.CharField(max_length=765)
    price = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    source = models.CharField(max_length=765)
    ranking = models.ForeignKey(Rank)
    url = models.URLField()
    category = models.ForeignKey(Category)
    comment = models.TextField(blank=True)
    quantity = models.IntegerField()
    #image_filename = models.CharField(max_length=765, blank=True)
    Image = models.ImageField(upload_to='itemimage')
#    class Meta:
#        db_table = u'Item'


class Message(models.Model):
    #messageid = models.IntegerField(primary_key=True)
    #sender = models.IntegerField()
    sender = models.ForeignKey(User, related_name='sender')
    #recipient = models.IntegerField()
    recipient = models.ForeignKey(User, related_name='recipient')    
    message = models.CharField(max_length=765)
    isread = models.IntegerField()
    created = models.DateField()
#    class Meta:
#        db_table = u'Message'


class Shopper(models.Model):
    #shopper = models.IntegerField(primary_key=True)
    #mayshopfor = models.IntegerField(primary_key=True)
    mayshopfor = models.ForeignKey('self')
    pending = models.IntegerField()
#    class Meta:
#        db_table = u'Shopper'

#class Users(models.Model):
#    userid = models.IntegerField(primary_key=True)
#    username = models.CharField(max_length=60)
#    password = models.CharField(max_length=150)
#    fullname = models.CharField(max_length=150)
#    email = models.CharField(max_length=765, blank=True)
#    approved = models.IntegerField()
#    admin = models.IntegerField()
#    comment = models.TextField(blank=True)
#    email_msgs = models.IntegerField()
#    list_stamp = models.DateTimeField(null=True, blank=True)
#    initialfamilyid = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = u'users'


# use the builtin Many to Many to build the automatic join

#class Membership(models.Model):
#    #userid = models.IntegerField(primary_key=True)
#    user = models.ForeignKey(User)
#    #familyid = models.IntegerField(primary_key=True)
#    familyid = models.ForeignKey(Family)
#    #familyid = models.ManyToManyField()
#    class Meta:
#        db_table = u'Membership'


class Alloc(models.Model):
    #itemid = models.IntegerField(primary_key=True)
    Item = models.ForeignKey(Item)
    #userid = models.IntegerField(primary_key=True)
    User = models.ForeignKey(User)
    #bought = models.IntegerField(primary_key=True)
    bought = models.IntegerField()
    quantity = models.IntegerField()
#    class Meta:
#        db_table = u'Alloc'

