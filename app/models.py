from django.db import models
from django.utils.translation import gettext_lazy as _


class WeaponGroup(models.Model):
    # ASSAULT_RIFFLE = 0
    # SHOTGUNS = 1
    # PISTOLS = 2
    # SMGS = 3
    # DRUM = 4
    # SNIPERS = 5
    # LAUNCHERS = 6

    id = models.AutoField(primary_key=True)
    name = models.CharField(_('Group name'), max_length=30)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    GRAY = 0
    GREEN = 1
    BLUE = 2
    PURPLE = 3
    GOLD = 4
    VARIANTS_CHOICES = (
        (GRAY, _('COMMON')),
        (GREEN, _('UNCOMMON')),
        (BLUE, _('RARE')),
        (PURPLE, _('EPIC')),
        (GOLD, _('LEGENDARY'))
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(_('Weapon name'), max_length=80, null=False, blank=False)
    variants = models.CharField(
        _('Variant'),
        max_length=10,
        choices=VARIANTS_CHOICES,
        default=GRAY
    )
    image = models.ImageField(_('Weapon image'))
    group = models.ForeignKey(
        to=WeaponGroup,
        verbose_name=_("Weapon group"),
        related_name='weapon',
        null=True,
        on_delete=models.SET_NULL
    )
    is_removed = models.BooleanField(_('Is removed ?'), default=False, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)


class ItemGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_('Group name'), max_length=30)

    def __str__(self):
        return self.name


class Item(models.Model):
    GRAY = 0
    GREEN = 1
    BLUE = 2
    PURPLE = 3
    GOLD = 4
    VARIANTS_CHOICES = (
        (GRAY, _('COMMON')),
        (GREEN, _('UNCOMMON')),
        (BLUE, _('RARE')),
        (PURPLE, _('EPIC')),
        (GOLD, _('LEGENDARY'))
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(_('Item name'), max_length=80, null=False, blank=False)
    variants = models.CharField(
        _('Variant'),
        max_length=10,
        choices=VARIANTS_CHOICES,
        default=GRAY
    )
    image = models.ImageField(_('Item image'))
    group = models.ForeignKey(
        to=ItemGroup,
        verbose_name=_('Item group'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='item'
    )
    is_removed = models.BooleanField(_('Is removed ?'), default=False, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)
