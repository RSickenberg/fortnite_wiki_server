import os

from django.conf import Settings

from app.models import Item, ItemDetail, ItemGroup, Weapon, WeaponDetail, WeaponGroup, LocationItem


class JsonData:

    def __init__(self, **data):
        self.weapons = data.get('data').get('weapons')
        self.items = data.get('data').get('items')
        self.weapons_details = data.get('data').get('details')
        self.items_details = data.get('data').get('itemDetails')

        self.weapon = None
        self.weapon_details = None
        self.item = None
        self.item_details = None

    def import_all(self):
        for weapon in self.weapons:
            self.import_weapon(weapon)
        for details in self.weapons_details:
            self.import_weapon_details(details)
        for item in self.items:
            self.import_item(item)
        for item_details in self.items_details:
            self.import_item_details(item_details)

    def import_weapon(self, weapon):
        self.weapon, _ = Weapon.objects.update_or_create(
            id=weapon.get('id'),
            defaults={
                'name': weapon.get('name'),
                'variants': weapon.get('color'),
                'image': weapon.get('img'),
                'group': WeaponGroup.objects.get(id__exact=weapon.get('group')),
                'is_removed': weapon.get('is_removed', False)
            }
        )
        print('[WEAPON] Imported: {}'.format(self.weapon))

    def import_weapon_details(self, details):
        self.weapon_details, _ = WeaponDetail.objects.update_or_create(
            detail_level=details.get('detailLevel'),
            weapon_id=Weapon.objects.get(id=details.get('weaponId')),
            defaults={
                'detail_level': details.get('detailLevel'),
                'weapon_id': Weapon.objects.get(id=details.get('weaponId')),
                'damage': details.get('damage'),
                'damage_head': details.get('damageHead'),
                'fire_rate': details.get('fireRate'),
                'magazine_size': details.get('magazineSize'),
                'reload_time': details.get('reloadTime'),
                'impact': details.get('impact'),
                'spread_base': details.get('spreadBase'),
                'spread_sprint': details.get('spreadSprint'),
                'spread_jump': details.get('spreadJump'),
                'spread_downsights': details.get('spreadDownsights'),
                'spread_standing': details.get('spreadStanding'),
                'spread_crouching': details.get('spreadCrouching'),
                'fire_rate_burst': details.get('firingRateBurst', 0.0),
                'environment_damages': details.get('environementDamage'),
                'recoil_horizontal': details.get('recoilHorizontal'),
                'recoil_vertical': details.get('recoilVertical'),
                'recoil_max_angle': details.get('recoilMaxAngle'),
                'recoil_min_angle': details.get('recoilMinAngle'),
                'recoil_downsights': details.get('recoilDownsights')
            }
        )
        print('[WEAPON_DETAILS] Imported: {}'.format(self.weapon_details))

    def import_item(self, item):
        self.item, _ = Item.objects.update_or_create(
            id=item.get('id'),
            defaults={
                'name': item.get('name'),
                'variants': item.get('color'),
                'image': item.get('img'),
                'group': ItemGroup.objects.get(id=item.get('group')),
                'is_removed': item.get('is_removed')
            }
        )
        print('[ITEM] Imported: {}'.format(self.item))

    def import_item_details(self, details):
        self.item_details, _ = ItemDetail.objects.update_or_create(
            item_id=Item.objects.get(id=details.get('itemId')),
            defaults={
                'is_heal': details.get('isHeal'),
                'is_explosive': details.get('isExplosive'),
                'shield': details.get('shield'),
                'heal': details.get('heal'),
                'damages': details.get('damages'),
                'delay': details.get('delay'),
                'capacity': details.get('capacity'),
                'comment': details.get('comment')
            }
        )
        # The goal is to deconstruct JSON "Ground, Chests, Supply" and link recent item to it.
        # Difficulty: String to location name
        for location in details.get('location').split(','):
            db_location, _ = LocationItem.objects.get_or_create(
                location__contains=location.replace(' ', ''),
                defaults={
                    'location': location
                }
            )
            self.item_details.location.add(db_location)

        self.item_details.save()

        print('[ITEM_DETAILS] Imported: {}'.format(self.item_details))
