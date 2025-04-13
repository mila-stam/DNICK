from django.contrib import admin
from .models import *
# Register your models here.

class MarketProductInline(admin.TabularInline):
    model = MarketProduct
    extra = 0


class MarketAdmin(admin.ModelAdmin):
    exclude=('user',)
    inlines = [MarketProductInline, ]
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class EmployeeAdmin(admin.ModelAdmin):
    exclude=('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EmployeeAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False
    
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['type', 'isHomemade']


admin.site.register(Market, MarketAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)