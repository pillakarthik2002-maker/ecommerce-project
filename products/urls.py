from django.urls import path

from .views import (
    product_list,
    product_detail,
    product_api,
    product_detail_api,
)


urlpatterns = [

    path(
        '',
        product_list,
        name='product_list'
    ),

    path(
        'api/',
        product_api,
        name='product_api'
    ),

    path(
        'api/<int:product_id>/',product_detail_api,
        name='product_detail_api'
    ),

    path(
        '<int:product_id>/',
        product_detail,
        name='product_detail'
    ),

]