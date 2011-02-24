from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^teste/$', 'teste.views.index'),
    (r'^teste/tweets/$', 'teste.views.tweets'),
    (r'^teste/mainPage/$', 'teste.views.mainPage'),
    (r'^admin/(.*)', admin.site.root),
)

