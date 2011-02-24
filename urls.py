from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^teste/$', 'Testando.teste.views.index'),
    (r'^teste/tweets/$', 'Testando.teste.views.tweets'),
    (r'^teste/mainPage/$', 'Testando.teste.views.mainPage'),
    (r'^admin/(.*)', admin.site.root),
)

