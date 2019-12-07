# from django.conf import settings
from django.contrib import admin
# from django.template.loader import get_template
# from django.urls import reverse

from .models import Weapon, WeaponGroup, ItemGroup, Item


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass


@admin.register(WeaponGroup)
class WeaponGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
