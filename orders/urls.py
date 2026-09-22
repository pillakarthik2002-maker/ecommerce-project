from django.urls import path

from .views import (
    checkout,
    order_confirmation,
    my_orders,
    order_detail,
)
from .views import (
    order_api,
    order_detail_api,
    checkout_api,
)


urlpatterns = [

    path(
        'checkout/',
        checkout,
        name='checkout'
    ),

    path(
        'confirmation/<int:order_id>/',
        order_confirmation,
        name='order_confirmation'
    ),

    path(
        'my-orders/',
        my_orders,
        name='my_orders'
    ),

    path(
        'my-orders/<int:order_id>/',
        order_detail,
        name='order_detail'
    ),

    path(
        'api/',
        order_api,
        name='order_api'
    ),

    path(
        'api/checkout/',
        checkout_api,
        name='checkout_api'
    ),

    path(
        'api/<int:order_id>/',
        order_detail_api,
        name='order_detail_api'
    ),


]