from django.contrib import admin

from .models import Item, ItemDetail, ItemGroup, LocationItem, Version, Weapon, WeaponDetail, WeaponGroup, Messages


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'variants', 'is_removed',)
    list_filter = ('variants', 'is_removed',)
    readonly_fields = ('last_update',)
    pass


@admin.register(WeaponDetail)
class WeaponDetailAdmin(admin.ModelAdmin):
    list_display = ('weapon_id', 'detail_level', 'damage',)
    list_filter = ('detail_level', 'weapon_id')
    readonly_fields = ('last_update',)
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'variants', 'is_removed',)
    list_filter = ('variants', 'is_removed', 'group',)
    readonly_fields = ('last_update',)
    pass


@admin.register(ItemDetail)
class ItemDetailAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'is_heal', 'is_explosive',)
    list_filter = ('is_heal', 'is_explosive', 'location',)
    readonly_fields = ('last_update',)
    pass


@admin.register(LocationItem)
class LocationItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')
    pass


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    pass


@admin.register(WeaponGroup)
class WeaponGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    pass


@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    pass


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('date', 'data')
    pass
