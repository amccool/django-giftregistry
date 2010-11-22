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
    
        