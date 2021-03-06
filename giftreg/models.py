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



class Category(models.Model):
    #categoryid = models.IntegerField(primary_key=True)
    #categoryid = models.IntegerField()
    CategoryName = models.CharField(max_length=150, blank=True)
#    class Meta:
#        db_table = u'Category'
    def __unicode__(self):
        return self.CategoryName

class Family(models.Model):
    #familyid = models.IntegerField(primary_key=True)
    FamilyName = models.CharField(max_length=765)
    FamilyMember = models.ManyToManyField(User)
#    class Meta:
#        db_table = u'Family'    
    def __unicode__(self):
        return self.FamilyName

class Event(models.Model):
    #eventid = models.IntegerField(primary_key=True)
    #userid = models.IntegerField(null=True, blank=True)
    User = models.ForeignKey(User)
    Family = models.ForeignKey(Family)
    description = models.CharField(max_length=300)
    eventdate = models.DateField()
    recurring = models.BooleanField()
#    class Meta:
#        db_table = u'Event'
    def __unicode__(self):
        return self.description


class Rank(models.Model):
    #ranking = models.IntegerField(primary_key=True)
    ranking = models.IntegerField()
    title = models.CharField(max_length=150)
    rendered = models.CharField(max_length=765)
    rankorder = models.IntegerField()
#    class Meta:
#        db_table = u'Rank'
    def __unicode__(self):
        return self.title


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
    image = models.ImageField(upload_to='itemimage')
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
    shopperUser = models.ForeignKey(User, related_name='shopperUser')
    #mayshopfor = models.IntegerField(primary_key=True)
    #mayshopfor = models.ForeignKey('self')
    mayshopfor = models.ForeignKey(User, related_name='mayshopfor')
    pending = models.BooleanField()
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



'''
User Profile Information
'''

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    birthday = models.DateField(blank=True, null=True)











