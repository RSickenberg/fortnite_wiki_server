from django.contrib import admin

from .models import Item, ItemDetail, ItemGroup, LocationItems, Weapon, WeaponDetail, WeaponGroup


@admin.register(WeaponGroup)
class WeaponGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass


@admin.register(WeaponDetail)
class WeaponDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemDetail)
class ItemDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(LocationItems)
class LocationAdmin(admin.ModelAdmin):
    pass
