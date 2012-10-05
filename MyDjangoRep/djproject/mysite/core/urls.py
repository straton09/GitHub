from django.conf.urls.defaults import *
from django.contrib import admin
from core.views import hello, cur_time, index, fulltext, post_comment
# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
                       ('^hello/$', hello),
                       ('^time/$', cur_time),
                       (r'^$', index),
                       (r'^fulltext/$', fulltext),
                       (r'^fulltext/thanks/$', post_comment),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

)
