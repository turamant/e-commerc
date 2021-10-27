# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import ShoppingCart, OrderInfo, OrderGoods

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ["user", "goods", "nums", ]

@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]

    '''class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]
'''


