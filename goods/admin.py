from django.contrib import admin

from goods.models import Categories, Products

# Register your models here.
#admin.site.register(Categories)
#admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """ Класс для пользовательского отображения таблицы Категория в админ панели """
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """ Класс для пользовательского отображения таблицы Продукт в админ панели """
    prepopulated_fields = {'slug': ('name', )}
