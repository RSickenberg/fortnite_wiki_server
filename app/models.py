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
    variants = models.IntegerField(
        _('Variant'),
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


class WeaponDetail(models.Model):
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
    detail_level = models.IntegerField(
        _('Level'),
        choices=VARIANTS_CHOICES,
        null=False,
        default=GRAY,
        blank=False
    )
    weapon_id = models.ForeignKey(
        to=Weapon,
        on_delete=models.SET_NULL,
        related_name='weapon',
        null=True,
        verbose_name=_('Related weapon')
    )
    damage = models.IntegerField(_('Damages'), null=False, blank=False)
    damage_head = models.FloatField(_('Damage head'), null=False, blank=False)
    fire_rate = models.FloatField(_('Fire rate'), null=False, blank=False)
    magazine_size = models.IntegerField(_('Magazine size'), null=False, blank=False)
    reload_time = models.FloatField(_('Reload time'), null=False, blank=False)
    impact = models.FloatField(_('Impact'), null=False, blank=False)

    spread_base = models.FloatField(_('Spread base'), null=False, blank=False)
    spread_sprint = models.FloatField(_('Spread sprint'), null=False, blank=False)
    spread_jump = models.FloatField(_('Spread jump'), null=False, blank=False)
    spread_downsights = models.FloatField(_('Spread downsights'), null=False, blank=False)
    spread_standing = models.FloatField(_('Spread standing'), null=False, blank=False)
    spread_crouching = models.FloatField(_('Spread crouching'), null=False, blank=False)

    fire_rate_burst = models.FloatField(_('Fire rate (burst)'), null=False, blank=False, help_text=_('May be removed.'))

    environement_damages = models.FloatField(_('Environmental damages'), null=False, blank=False)

    recoil_horizontal = models.FloatField(_('Recoil horizontal'), null=False, blank=False)
    recoil_vertical = models.FloatField(_('Recoil vertical'), null=False, blank=False)
    recoil_max_angle = models.FloatField(_('Recoil max angle'), null=False, blank=False)
    recoil_min_angle = models.FloatField(_('Recoil min angle'), null=False, blank=False)
    recoil_downsights = models.FloatField(_('Recoil downsights'), null=False, blank=False)

    def __str__(self):
        return "Details for weapon [{}] with level: {}".format(self.weapon_id.name, self.detail_level)


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
    variants = models.IntegerField(
        _('Variant'),
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


class LocationItems(models.Model):
    # GROUND = 'G'
    # CHEST = 'C'
    # VENDING = 'V'
    # SUPPLIES = 'S'
    # LAMAS = 'L'
    # LOCATION_CHOICES = (
    #     (GROUND, _('Ground')),
    #     (CHEST, _('Chests')),
    #     (VENDING, _('Vending')),
    #     (SUPPLIES, _('Supply')),
    #     (LAMAS, _('LAMAS'))
    # )
    location = models.CharField(_('Location'), blank=True, null=False, max_length=90)

    def __str__(self):
        return '{}'.format(self.location)


class ItemDetail(models.Model):
    item_id = models.ForeignKey(
        to=Item,
        on_delete=models.SET_NULL,
        verbose_name=_('Related item'),
        null=True,
        related_name='item'
    )
    is_heal = models.BooleanField(_('Is heal ?'), default=False, null=False, blank=False)
    is_explosive = models.BooleanField(_('Is explosive ?'), default=False, null=False, blank=False)
    heal = models.IntegerField(_('Heal'), null=False, blank=False)
    shield = models.IntegerField(_('Shield'), null=False, blank=False)
    delay = models.FloatField(_('Delay'), null=False, blank=False)
    damages = models.IntegerField(_('Damages'), null=False, blank=False)
    location = models.ManyToManyField(
        to=LocationItems,
        verbose_name=_('Location'),
        blank=True,
        related_name='item_detail'
    )
    capacity = models.IntegerField(_('Capacity'), null=False, blank=False)
    comment = models.TextField(_('Comments'), null=False, blank=True)

    def __str__(self):
        return '[{}] details'.format(self.item_id.name)