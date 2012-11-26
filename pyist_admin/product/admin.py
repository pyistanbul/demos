# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from product.models import Product, Category

class CategoryInline(admin.TabularInline):
    model = Product
    extra = 5
    exclude = ('description',)

class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug' : ('name',)}

    inlines = (CategoryInline,)


class ProductCustomFilter(SimpleListFilter):

    title = u'Product Custom'

    parameter_name = 'prodcut_custom'

    def lookups(self, request, model_admin):
        return ( ('0',u'120 TL Üzerinde'),
                 ('1',u'120 Tl Altında')
                )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(price__gt = 120)

        if self.value() == '1':
            return queryset.filter(price__lt = 120)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','price_with_unit','active')

    def price_with_unit(self, obj):
        return '%s TL' % obj.price

    price_with_unit.short_description = u'Toplam Fiyat'
    price_with_unit.admin_order_field = 'price'

    list_editable = ('active',)



    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    actions = ('product_passive',)

    def product_passive(self, request, queryset):
        queryset.update(active = False)

    product_passive.short_description = u'Pasif Yap'

    list_filter = ('category',ProductCustomFilter)




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)