# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length = 255, verbose_name = u'Kategori İsmi')
    slug = models.SlugField(max_length = 255, verbose_name = u'Kategori Slug')
    description = models.TextField(verbose_name=u'Açıklama', null = True, blank = True)
    active = models.BooleanField(verbose_name = u'Aktif', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Kategori')
        verbose_name_plural = _(u'Kategoriler')




class Product(models.Model):
    name = models.CharField(max_length = 255, verbose_name = u'Ürün İsmi')
    slug = models.SlugField(max_length = 255, verbose_name = u'Ürün Slug',
                            help_text=u'Ürün ismini yazarken otomatik olarak bu alan doldurulucaktır.')
    category = models.ForeignKey(Category,null = True, blank = True, verbose_name = u'Kategori')
    description = models.TextField(verbose_name=u'Açıklama', null = True, blank = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 10, verbose_name = u'Ürün Fiyatı',
                                help_text=u'Ürünün fiyatını giriniz.')
    kdv = models.DecimalField(decimal_places = 2, max_digits = 10, verbose_name = u'KDV Fiyatı',
                              help_text=u'Ürünün kdv tutarını giriniz.')
    total_price = models.DecimalField(decimal_places = 2, max_digits = 10, verbose_name = u'Toplam Fiyatı')
    order = models.IntegerField(default = 0, verbose_name = u'Ürün Sıralması')
    active = models.BooleanField(verbose_name = u'Aktif', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Ürün')
        verbose_name_plural = _(u'Ürünler')

