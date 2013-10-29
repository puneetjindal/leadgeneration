from django import template
from django.shortcuts import render_to_response
from django.template import RequestContext
from crm.models import Client

def lg_listing(request):
    all_lg = Client.objects.all()
    return render_to_response(
        'lg_listing.html', {
            'all_lg': all_lg},
        context_instance=RequestContext(request))