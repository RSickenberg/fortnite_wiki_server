from app.models import Item, ItemDetail, ItemGroup, LocationItem, Weapon, WeaponDetail, WeaponGroup, Version


class JsonData:

    def __init__(self, **data):
        self.weapons = data.get('data').get('weapons')
        self.items = data.get('data').get('items')
        self.locations = data.get('data').get('locations')
        self.weapons_details = data.get('data').get('details')
        self.items_details = data.get('data').get('itemDetails')
        self.version = data.get('data').get('version')
        self.season = data.get('data').get('season')

        self.weapon = None
        self.weapon_details = None
        self.location = None
        self.item = None
        self.item_details = None

    def import_all(self):
        for weapon in self.weapons:
            self.import_weapon(weapon)
        for details in self.weapons_details:
            self.import_weapon_details(details)
        for location in self.locations:
            self.import_locations(location)
        for item in self.items:
            self.import_item(item)
        for item_details in self.items_details:
            self.import_item_details(item_details)
        self.import_season_version(self.version, self.season)

    def import_weapon(self, weapon):
        self.weapon, _ = Weapon.objects.update_or_create(
            id=weapon.get('id'),
            defaults={
                'name': weapon.get('name'),
                'variants': weapon.get('variants'),
                'image': weapon.get('image'),
                'group': WeaponGroup.objects.get(id__exact=weapon.get('group')),
                'is_removed': weapon.get('is_removed', False),
                'is_incomplete': weapon.get('is_incomplete', False)
            }
        )
        print('[WEAPON] Imported: {}'.format(self.weapon))

    def import_weapon_details(self, details):
        self.weapon_details, _ = WeaponDetail.objects.update_or_create(
            detail_level=details.get('detail_level'),
            weapon_id=Weapon.objects.get(id=details.get('weapon_id')),
            defaults={
                'detail_level': details.get('detail_level'),
                'weapon_id': Weapon.objects.get(id=details.get('weapon_id')),
                'damage': details.get('damage'),
                'damage_head': details.get('damage_head'),
                'fire_rate': details.get('fire_rate'),
                'magazine_size': details.get('magazine_size'),
                'reload_time': details.get('reload_time'),
                'impact': details.get('impact'),
                'spread_base': details.get('spread_base'),
                'spread_sprint': details.get('spread_sprint'),
                'spread_jump': details.get('spread_jump'),
                'spread_downsights': details.get('spread_downsights'),
                'spread_standing': details.get('spread_standing'),
                'spread_crouching': details.get('spread_crouching'),
                'fire_rate_burst': details.get('firing_rate_burst', 0.0),
                'environment_damages': details.get('environment_damages'),
                'recoil_horizontal': details.get('recoil_horizontal'),
                'recoil_vertical': details.get('recoil_vertical'),
                'recoil_max_angle': details.get('recoil_max_angle'),
                'recoil_min_angle': details.get('recoil_min_angle'),
                'recoil_downsights': details.get('recoil_downsights')
            }
        )
        print('[WEAPON_DETAILS] Imported: {}'.format(self.weapon_details))

    def import_locations(self, location):
        self.location, _ = LocationItem.objects.update_or_create(
            id=location.get('id'),
            defaults={
                'location': location.get('location')
            }
        )
        print('[LOCATIONS] Imported: {}'.format(self.location))

    def import_item(self, item):
        self.item, _ = Item.objects.update_or_create(
            id=item.get('id'),
            defaults={
                'name': item.get('name'),
                'variants': item.get('variants'),
                'image': item.get('image'),
                'group': ItemGroup.objects.get(id=item.get('group')),
                'is_removed': item.get('is_removed'),
                'is_incomplete': item.get('is_incomplete', False)
            }
        )
        print('[ITEM] Imported: {}'.format(self.item))

    def import_item_details(self, details):
        self.item_details, _ = ItemDetail.objects.update_or_create(
            item_id=Item.objects.get(id=details.get('item_id')),
            defaults={
                'is_heal': details.get('is_heal'),
                'is_explosive': details.get('is_explosive'),
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
        # Legacy code no more used
        # for location in details.get('location').split(','):
        #     db_location, created = LocationItem.objects.get_or_create(
        #         location__contains=location.strip(),
        #         defaults={
        #             'location': location.strip()
        #         }
        #     )
        #     if created:
        #         print('[LOCATION] Created: {}'.format(db_location.location))
        #
        #     self.item_details.location.add(db_location)

        for location in details.get('location'):
            db_location = LocationItem.objects.get(
                pk=location
            )

            if db_location:
                self.item_details.location.add(db_location)
                self.item_details.save()
        print('[ITEM_DETAILS] Imported: {}'.format(self.item_details))

    def import_season_version(self, version, season):
        self.version, _ = Version.objects.update_or_create(
            version=version,
            season=season,
            defaults={
                'season': season,
                'version': version
            }
        )
        print('[SEASON + VERSION] Imported: {}!'.format(self.version))
