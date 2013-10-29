from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^client/listing/', 'crm.views.lg_listing'),
)