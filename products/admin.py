from django.contrib import admin
from products.models import *

# Register your models here.
@admin.register(CPUInfo)
class CPUInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_name', 'clock_rate', 'l2_cache', 'l3_cache', 'core', 'threads', 'gpu', 'features',)
    list_filter = ('manufacture', 'announce_date', 'technology', 'socket',)
    search_fields = ('name',)
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'announce_date'
    ordering = ('name', 'created_at')


@admin.register(RAMInfo)
class RAMInfoAdmin(admin.ModelAdmin):
    # list_display = ('__all__',)
    # list_filter = ('__all__',)
    search_fields = ('name',)
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('name', 'created_at')


@admin.register(VGAInfo)
class VGAInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'pipelines',
                    'core_speed', 'memory_speed', 'memory_bus_width', 'direct_x', 'technology', 'features',)
    list_filter = ('use_type', 'manufacturer', 'architecture',)
    search_fields = ('name',)
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'release_date'
    ordering = ('name', 'created_at')


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'screen_resolution',
                    'cpu', 'memory_type', 'memory_size', 'vga', 'os', 'pin', 'weight',)
    list_filter = ('brand', 'os', 'screen_resolution',)
    raw_id_fields = ('vga', 'cpu',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    ordering = ('name', 'created_at')
