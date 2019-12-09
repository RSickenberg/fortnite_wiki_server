from django.core import serializers
from django.http import JsonResponse

from .models import Item, ItemDetail, LocationItem, Version, Weapon, WeaponDetail


def json_response(request):
    # Serialise all models to a Json file like in prod.
    version = Version.objects.latest('pk').version
    weapons = [
        {**weapon['fields'], 'id': weapon['pk']} for weapon in serializers.serialize('python', Weapon.objects.all())
    ]
    items = [
        {**item['fields'], 'id': item['pk']} for item in serializers.serialize('python', Item.objects.all())
    ]
    weapons_details = [
        {**details['fields']} for details in serializers.serialize('python', WeaponDetail.objects.all())
    ]
    items_details = [
        {**details['fields']} for details in serializers.serialize('python', ItemDetail.objects.all())
    ]
    locations = [
        {**locations['fields'], 'id': locations['pk']} for locations in serializers.serialize('python',
                                                                                              LocationItem.objects.all()
                                                                                              )
    ]

    return JsonResponse(
        {'version': "{}".format(version), 'weapons': weapons, 'items': items, 'details':
            weapons_details, 'itemDetails': items_details, 'locations': locations,
         }, safe=True, content_type='application/json'
    )
