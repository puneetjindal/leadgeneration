from django import template
from wms.app_settings import SK_DELIMITER
register = template.Library()
from oms.utils import get_invoice_slip_url, get_packing_slip_url
from oms.utils import get_main_packing_slip_url, get_main_invoice_slip_url


@register.filter(name='invoice_url')
def tt_invoice_url(client_store_sk, shipment_id):
    return get_invoice_slip_url(client_store_sk, shipment_id)


@register.filter()
def packing_url(client_store_sk, shipment_id):
    return get_packing_slip_url(client_store_sk, shipment_id)


@register.simple_tag()
def get_main_packing_slip(client_store_sk, *args, **kwargs):
    return get_main_packing_slip_url(client_store_sk, *args, **kwargs)


@register.simple_tag()
def get_main_invoice_slip(client_store_sk, *args, **kwargs):
    return get_main_invoice_slip_url(client_store_sk, *args, **kwargs)
