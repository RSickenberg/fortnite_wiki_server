from django.core import serializers
from django.http import JsonResponse

from .models import Item, ItemDetail, LocationItem, Version, Weapon, WeaponDetail, Messages


def json_response(request):
    # Serialise all models to a Json file like in prod.
    update = Version.objects.latest('pk')
    weapons = [
        {**weapon['fields'], 'id': weapon['pk']} for weapon in serializers.serialize('python',
                                                                                     Weapon.objects.order_by('id').all())
    ]
    items = [
        {**item['fields'], 'id': item['pk']} for item in serializers.serialize('python', Item.objects.order_by('id').all())
    ]
    weapons_details = [
        {**details['fields']} for details in serializers.serialize('python', WeaponDetail.objects.order_by(
            'weapon_id').order_by('detail_level').all())
    ]
    items_details = [
        {**details['fields']} for details in serializers.serialize('python', ItemDetail.objects.order_by(
            'item_id').all())
    ]
    locations = [
        {**locations['fields'], 'id': locations['pk']} for locations in serializers.serialize('python',
                                                                                              LocationItem.objects.all()
                                                                                              )
    ]

    return JsonResponse(
        {'version': "{}".format(update.version), 'season': '{}'.format(update.season), 'weapons': weapons,
         'items': items, 'details': weapons_details, 'itemDetails': items_details, 'locations': locations,
         }, content_type='application/json'
    )


def view_messages(request):
    messages = [
        {**message['fields']} for message in serializers.serialize('python', Messages.objects.all())
    ]

    return JsonResponse(messages, safe=False)
