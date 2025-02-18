from django.contrib import admin
from .models import Product, NetworkNode

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Настройка для отображения класса Product на админ панели
    """
    list_display = ('name', 'model', 'release_date')


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    """
    Настройка для отображения класса NetworkNode на админ панели, возможности фильтрации по городу и возможности
    убрать долг
    """
    list_display = ('name', 'city', 'supplier_link', 'debt', 'level', 'created_at')
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
    clear_debt.short_description = "Очистить задолженность у выбранных объектов"
