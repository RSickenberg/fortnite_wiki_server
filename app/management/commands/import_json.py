import requests
import json

from django.conf import settings
from django.core.management.base import BaseCommand

from app.management.helpers.json_data import JsonData


class Command(BaseCommand):
    help = 'Sync JSON from prod to Django app'
    errors = []

    def handle(self, *args, **options):
        self.import_json()

        if len(self.errors) > 0:
            self.stderr.write('Somme errors happened during sync: \n')
            for error in self.errors:
                self.stderr.write('- {}. \n'.format(error.message))

    def import_json(self):
        self.stdout.write('Importing JSON ...')
        req = requests.get(settings.JSON_PROD_URL)
        data = json.loads(req.content.decode())

        site = JsonData(data=data)
        site.import_all()

        req.close()
