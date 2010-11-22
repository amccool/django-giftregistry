from django.conf.urls.defaults import *
from giftreg import views

# maps url patterns to methods in views.py
urlpatterns = patterns(
    '',
    (r'^$', views.index),
    #(r'^giftreg/$', index),
    #(r'^index/$', index),

    (r'^categories/$', views.categories),
    
    (r'^ranks/$', views.ranks),
    (r'^ranks/rank/add$', views.rankAdd),
    (r'^ranks/rank/edit/(?P<rankid>\d+)$', views.rankEdit),
    (r'^ranks/rank/delete/(?P<rankid>\d+)$', views.rankDelete),
    (r'^ranks/rank/promote/(?P<rankid>\d+)$', views.rankPromote),
    (r'^ranks/rank/demote/(?P<rankid>\d+)$', views.rankDemote),


    (r'^item/add/$', views.itemAdd),

    (r'^shoppinglist/$', views.shoppinglist),
    (r'^mylist/$', views.mylist),

    (r'^event/$', views.event),
    (r'^families/$', views.families),

    #handle users through the admin pages
    #(r'^users/$', views.users),
)
