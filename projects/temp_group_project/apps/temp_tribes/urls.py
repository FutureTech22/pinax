from django.conf.urls.defaults import *

from temp_tribes.models import Tribe
from wiki import models as wiki_models

wiki_args = {'group_slug_field': 'slug',
             'group_qs': Tribe.objects.filter(deleted=False)}


urlpatterns = \
    patterns('',
        url(r'^create/$', 'temp_tribes.views.create', name="tribe_create"),
        url(r'^your_tribes/$', 'temp_tribes.views.your_tribes', name="your_tribes"),
        
        url(r'^$', 'temp_tribes.views.tribes', name="tribe_list"),
        url(r'^order/topics/least-topics/$', 'temp_tribes.views.tribes',
            {'order': 'least_topics'}, name="tribe_list_least_topics"),
        url(r'^order/topics/most-topics/$', 'temp_tribes.views.tribes',
            {'order': 'most_topics'}, name="tribe_list_most_topics"),
        url(r'^order/members/least-members/$', 'temp_tribes.views.tribes',
            {'order': 'least_members'}, name="tribe_list_least_members"),
        url(r'^order/members/most-members/$', 'temp_tribes.views.tribes',
            {'order': 'most_members'}, name="tribe_list_most_members"),
        url(r'^order/name/ascending/$', 'temp_tribes.views.tribes',
            {'order': 'name_ascending'}, name="tribe_list_name_ascending"),
        url(r'^order/name/descending/$', 'temp_tribes.views.tribes',
            {'order': 'name_descending'}, name="tribe_list_name_descending"),
        url(r'^order/date/oldest/$', 'temp_tribes.views.tribes',
            {'order': 'date_oldest'}, name="tribe_list_date_oldest"),
        url(r'^order/date/newest/$', 'temp_tribes.views.tribes',
            {'order': 'date_newest'}, name="tribe_list_date_newest"),
        
        # tribe-specific
        url(r'^tribe/([-\w]+)/$', 'temp_tribes.views.tribe', name="tribe_detail"),
        url(r'^tribe/([-\w]+)/delete/$', 'temp_tribes.views.delete', name="tribe_delete"),
        
        # topics
        url(r'^tribe/([-\w]+)/topics/$', 'temp_tribes.views.topics', name="tribe_topics"),
        url(r'^topic/(\d+)/edit/$', 'temp_tribes.views.topic', kwargs={"edit": True}, name="tribe_topic_edit"),
        url(r'^topic/(\d+)/delete/$', 'temp_tribes.views.topic_delete', name="tribe_topic_delete"),
        url(r'^topic/(\d+)/$', 'temp_tribes.views.topic', name="tribe_topic"),
        
        # wiki
        url(r'^tribe/(?P<group_slug>\w+)/wiki/', include('wiki.urls'), kwargs=wiki_args),
    )