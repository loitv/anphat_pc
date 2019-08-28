from django.contrib import admin
from products.models import *

# Register your models here.
@admin.register(CPUInfo)
class CPUInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_name', 'clock_rate', 'l2_cache', 'l3_cache', 'core', 'threads', 'gpu', 'features',)
    list_filter = ('manufacture', 'announce_date', 'technology', 'socket',)
    search_fields = ('name', 'non_white_space_name',)
    prepopulated_fields = {'non_white_space_name': ('name',)}
    readonly_fields = ('non_white_space_name',)
    date_hierarchy = 'announce_date'
    ordering = ('name', 'created_at')


@admin.register(RAMInfo)
class RAMInfoAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    ordering = ('name', 'created_at')


@admin.register(VGAInfo)
class VGAInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'pipelines',
                    'core_speed', 'memory_speed', 'memory_bus_width', 'direct_x', 'technology', 'features',)
    list_filter = ('use_type', 'manufacturer', 'architecture',)
    search_fields = ('name', 'non_white_space_name',)
    readonly_fields = ('non_white_space_name',)
    date_hierarchy = 'release_date'
    ordering = ('name', 'created_at')


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.non_white_space_name = ''.join(form.cleaned_data['name'].lower().split(' '))
        obj.save()

    list_display = ('name', 'brand', 'cpu', 'vga', 'os', 'pin', 'weight',)
    list_filter = ('brand', 'os',)
    raw_id_fields = ('vga', 'cpu',)
    search_fields = ('name', 'non_white_space_name',)
    readonly_fields=('non_white_space_name',)
    date_hierarchy = 'created_at'
    ordering = ('name', 'created_at')
