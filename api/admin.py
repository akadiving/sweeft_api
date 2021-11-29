from django.contrib import admin
from .models import Activity, Category
# Register your models here.

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'activity', 'type', 'price',
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name'
    ]
