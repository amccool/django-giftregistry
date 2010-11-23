from django.conf.urls.defaults import *
#from django.contrib.auth.views import login, logout
from django.conf import settings

import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^giftReg/', include('giftreg.urls')),
    
    (r'^$', views.index),
    

    # auth
    #(r'^accounts/', include('registration.backends.default.urls')),    
    (r'^accounts/', include('registration.urls')),
    #(r'^accounts/login/$', login),
    #(r'^accounts/logout/$', logout),    
    
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    
    

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^currencies/', include('currencies.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),    
)
