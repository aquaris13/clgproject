from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scheme', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('name',)
