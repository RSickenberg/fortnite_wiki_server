from io import StringIO

from django.core import management
from django.core.management import BaseCommand
from django.db import connection


def reset_db():
    """
    Reset database to a blank state by removing all the tables and recreating them.
    """
    with connection.cursor() as cursor:
        cursor = connection.cursor()
        cursor.execute('show tables;')
        parts = ('DROP TABLE IF EXISTS %s;' % table for (table,) in cursor.fetchall())
        sql = 'SET FOREIGN_KEY_CHECKS = 0;\n' + '\n'.join(parts) + 'SET FOREIGN_KEY_CHECKS = 1;\n'
        connection.cursor().execute(sql)

        management.call_command('migrate', stdout=StringIO())


class Command(BaseCommand):
    help = 'Reset the Database and load fixtures'

    def add_arguments(self, parser):
        parser.add_argument('-y', '--yes', action='store_true', dest='force_yes', default=False, help='Don\' ask for '
                                                                                                      'confirmation')
        parser.add_argument('-s', '--sync', action='store_true', dest='sync_json', default=True, help='Import json at '
                                                                                                      'the end')

        parser.add_argument('-n', '--no-reset', action='store_true', dest='no_reset', default=False,
                            help="Avoid DB reset, directly go on with fixtures and sync.")

    def handle(self, *args, **options):
        if not options['force_yes']:
            self.stdout.write(self.style.WARNING("WARNING") + "\nThis will remove ALL EXISTING DATA from the "
                                                              "database. \n"
                                                              "Are you SURE you want to do that? (y/n) \n",
                              ending=''
                              )
            try:
                result = input()
            except KeyboardInterrupt:
                self.stdout.write("Aborting.")
                return

            if result.lower() != 'y':
                self.stdout.write("Aborting.")
                return
        if not options['no_reset']:
            self.stdout.write("Resetting the database... ", ending='')
            self.stdout.flush()
            reset_db()

        self.stdout.write(self.style.SUCCESS("OK"))
        self.stdout.write("Loading fixtures ... ", ending='')
        management.call_command('loaddata', 'item_group', format='json', app='app', stdout=StringIO())
        management.call_command('loaddata', 'weapon_group', format='json', app='app', stdout=StringIO())
        self.stdout.write(self.style.SUCCESS("OK"))

        if options['sync_json']:
            management.call_command('import_json')
            self.stdout.write(self.style.SUCCESS("OK"))
