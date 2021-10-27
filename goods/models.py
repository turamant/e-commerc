# _*_coding:utf-8_*_

from datetime import datetime

from django.db import models

class GoodsCategory(models.Model):
    """
Product category
    """
    CATEGORY_TYPE = (
        (1, "First Class"),
        (2, "Class 2"),
        (3, "Three-level category"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="Category name", help_text="Category name ")
    code = models.CharField(default="", max_length=30, verbose_name="Category code", help_text="Category code ")
    desc = models.TextField(default="", verbose_name="Category description", help_text="Category description ")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="Category level",
                                        help_text="Category level")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="Parent Category Level",
                                        help_text="Parent Directory",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="Whether to navigate", help_text="Whether to navigate")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "Commodity Category"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
Brand name
    """
    category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True,
                                 verbose_name="Commodity Category", on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=30, verbose_name="Brand name", help_text="Brand name ")
    desc = models.TextField(default="", max_length=200, verbose_name="Brand description",
                            help_text="Brand description ")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
Commodities
    """
    category = models.ForeignKey(GoodsCategory, verbose_name="Commodity Category", on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=50, default="", verbose_name="Commodity unique article number ")
    name = models.CharField(max_length=100, verbose_name="Product name")
    click_num = models.IntegerField(default=0, verbose_name="Clicks")
    sold_num = models.IntegerField(default=0, verbose_name="Commodity Sales")
    fav_num = models.IntegerField(default=0, verbose_name="Number of Favorites")
    goods_num = models.IntegerField(default=0, verbose_name="Inventory")
    market_price = models.FloatField(default=0, verbose_name="market price")
    shop_price = models.FloatField(default=0, verbose_name="Our shop price")
    goods_brief = models.TextField(max_length=500, verbose_name="Description of the product")
    ship_free = models.BooleanField(default=True, verbose_name="Whether to bear freight")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True,
                                          verbose_name="cover picture")
    is_new = models.BooleanField(default=False, verbose_name="Is it new?")
    is_hot = models.BooleanField(default=False, verbose_name="Whether it sells well")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = 'commodity'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category', verbose_name="Commodity Category",
                                 on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, related_name='goods', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Home Product Category Advertisement'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    """
Merchandise carousel map
    """
    goods = models.ForeignKey(Goods, verbose_name="commodity", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", verbose_name="Image ", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = 'product picture'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
Carousel products
    """
    goods = models.ForeignKey(Goods, verbose_name="commodity", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name="Carousel pictures")
    index = models.IntegerField(default=0, verbose_name="Carousel Order")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = 'Carousel goods'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
Hot word search
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="Hot Words ")
    index = models.IntegerField(default=0, verbose_name="Sort")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = 'Hot word search'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords