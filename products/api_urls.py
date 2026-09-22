from django.urls import path

from .views import (
    product_api,
    product_detail_api,
)


urlpatterns = [

    path(
        '',
        product_api,
        name='product_api'
    ),

    path(
        '<int:product_id>/',
        product_detail_api,
        name='product_detail_api'
    ),

]