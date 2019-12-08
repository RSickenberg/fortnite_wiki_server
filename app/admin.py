from django.contrib import admin

from .models import Item, ItemDetail, ItemGroup, LocationItem, Weapon, WeaponDetail, WeaponGroup, Version


# @admin.register(WeaponGroup)
# class WeaponGroupAdmin(admin.ModelAdmin):
#     pass


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'variants', 'is_removed',)
    list_filter = ('variants', 'is_removed',)
    pass


@admin.register(WeaponDetail)
class WeaponDetailAdmin(admin.ModelAdmin):
    list_display = ('weapon_id', 'detail_level', 'damage',)
    list_filter = ('detail_level',)
    pass


# @admin.register(ItemGroup)
# class ItemGroupAdmin(admin.ModelAdmin):
#     pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'variants', 'is_removed',)
    list_filter = ('variants', 'is_removed',)
    pass


@admin.register(ItemDetail)
class ItemDetailAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'is_heal', 'is_explosive',)
    list_filter = ('is_heal', 'is_explosive',)
    pass


# @admin.register(LocationItem)
# class LocationItemsAdmin(admin.ModelAdmin):
#     pass


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    pass