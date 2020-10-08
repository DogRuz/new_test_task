from task.views import get_list_categories, get_list_active_company, get_list_active_product, get_product_detail_card, \
    changes_company, insert_product, changes_product, insert_company, changes_category, insert_category
from django.conf.urls import url

urlpatterns = [
    url(r'^get_list_categories/?$', get_list_categories),
    url(r'^get_list_active_company/?$', get_list_active_company),
    url(r'^get_list_active_product/?$', get_list_active_product),
    url(r'^get_product_detail_card/(?P<pk>[0-9]+)?$', get_product_detail_card),
    url(r'^changes_company/(?P<pk>[0-9]+)?$', changes_company),
    url(r'^insert_company/', insert_company),
    url(r'^changes_product/(?P<pk>[0-9]+)?$', changes_product),
    url(r'^insert_product/?$', insert_product),
    url(r'^changes_category/(?P<pk>[0-9]+)?$', changes_category),
    url(r'^insert_category/?$', insert_category),
]