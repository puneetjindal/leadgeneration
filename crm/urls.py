from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^client/listing/', 'crm.views.lg_listing'),
)