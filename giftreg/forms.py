'''
Created on Mar 19, 2010

@author: amccool
'''

from django.db import models
from django.forms import ModelForm, Form
from django import forms

import models

class CategoryForm(ModelForm):
    '''
    classdocs
    '''
    class Meta:
        model = models.Category

#    def __init__(selfparams):
#        '''
#        Constructor
#        '''
        
class RankForm(ModelForm):
    '''
    classdocs
    '''
    class Meta:
        model = models.Rank

#    def __init__(selfparams):
#        '''
#        Constructor
#        '''    


class FamilyForm(ModelForm):
    '''
    classdocs
    '''
    class Meta:
        model = models.Family

#    def __init__(selfparams):
#        '''
#        Constructor
#        '''   

class EventForm(ModelForm):
    '''
    classdocs
    '''
    class Meta:
        model = models.Event

#    def __init__(selfparams):
#        '''
#        Constructor
#        '''   
        
        
        
class ItemAddModelForm(ModelForm):
    '''
    classdocs
    '''
    source = forms.CharField(label='Store/Retailer')
    #user = forms.ModelChoiceField(widget=forms.HiddenInput())
    url = forms.URLField(required=False)
    image = forms.ImageField(required=False)
    class Meta:
        model = models.Item
        exclude = ('User',)
        
class ItemAddForm(Form):
    Description = forms.CharField()
    
    
    
#class ProfileForm(ModelForm):
#    def __init__(self, *args, **kwargs):
#        super(ProfileForm, self).__init__(*args, **kwargs)
#        try:
#            self.fields['email'].initial = self.instance.user.email
#        except User.DoesNotExist:
#            pass
#
#    email = forms.EmailField(label="Primary email")
#
#    class Meta:
#      model = model
#
#    def save(self, *args, **kwargs):
#      """
#      Update the primary email address on the related User object as well. 
#      """
#      u = self.instance.user
#      u.email = self.cleaned_data['email']
#      u.save()
#      profile = super(ProfileForm, self).save(*args,**kwargs)
#      return profile    
    
        