from django.contrib import admin
from products.models import *

# Register your models here.
@admin.register(CPUInfo)
class CPUInfoAdmin(admin.ModelAdmin):
    # list_display = ('__all__',)
    # list_filter = ('__all__',)
    # search_fields = ('__all__',)
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('name', 'created_at')


@admin.register(RAMInfo)
class RAMInfoAdmin(admin.ModelAdmin):
    # list_display = ('__all__',)
    # list_filter = ('__all__',)
    # search_fields = ('__all__',)
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('name', 'created_at')


@admin.register(VGAInfo)
class VGAInfoAdmin(admin.ModelAdmin):
    # list_display = ('__all__',)
    # list_filter = ('__all__',)
    # search_fields = ('__all__',)
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('name', 'created_at')


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'screen_resolution',
                    'cpu', 'memory_type', 'memory_size', 'vga', 'os', 'pin', 'weight',)
    # list_filter = ('__all__',)
    # search_fields = ('__all__',)
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('name', 'created_at')
