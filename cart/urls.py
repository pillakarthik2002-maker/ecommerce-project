from django.urls import path

from .views import (
    add_to_cart,
    cart_detail,
    update_cart,
    remove_from_cart,
)
from .views import (
    cart_api,
    cart_add_api,
    cart_update_api,
    cart_remove_api,
)


urlpatterns = [

    path(
        'add/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        '',
        cart_detail,
        name='cart_detail'
    ),

    path(
        'update/<int:item_id>/',
        update_cart,
        name='update_cart'
    ),

    path(
        'remove/<int:item_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),
        path(
        'api/',
        cart_api,
        name='cart_api'
    ),

    path(
        'api/add/',
        cart_add_api,
        name='cart_add_api'
    ),

    path(
        'api/update/<int:item_id>/',
        cart_update_api,
        name='cart_update_api'
    ),

    path(
        'api/remove/<int:item_id>/',
        cart_remove_api,
        name='cart_remove_api'
    ),

]