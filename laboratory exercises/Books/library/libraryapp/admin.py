from django.contrib import admin
from .models import *

# Register your models here.
class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0

class GenreAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
    def has_delete_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        return False

class BookAdmin(admin.ModelAdmin): 
    inlines = [RatingInline,]
    exclude = ('user',)
    list_filter = ["isAvail",]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)
    
    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False
    
class RatingAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False
    
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
