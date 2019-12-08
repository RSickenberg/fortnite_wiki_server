# Generated by Django 3.0 on 2019-12-08 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191207_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=90, verbose_name='Location')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='variants',
            field=models.IntegerField(choices=[(0, 'COMMON'), (1, 'UNCOMMON'), (2, 'RARE'), (3, 'EPIC'), (4, 'LEGENDARY')], default=0, verbose_name='Variant'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='variants',
            field=models.IntegerField(choices=[(0, 'COMMON'), (1, 'UNCOMMON'), (2, 'RARE'), (3, 'EPIC'), (4, 'LEGENDARY')], default=0, verbose_name='Variant'),
        ),
        migrations.CreateModel(
            name='WeaponDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_level', models.IntegerField(choices=[(0, 'COMMON'), (1, 'UNCOMMON'), (2, 'RARE'), (3, 'EPIC'), (4, 'LEGENDARY')], default=0, verbose_name='Level')),
                ('damage', models.IntegerField(verbose_name='Damages')),
                ('damage_head', models.FloatField(verbose_name='Damage head')),
                ('fire_rate', models.FloatField(verbose_name='Fire rate')),
                ('magazine_size', models.IntegerField(verbose_name='Magazine size')),
                ('reload_time', models.FloatField(verbose_name='Reload time')),
                ('impact', models.FloatField(verbose_name='Impact')),
                ('spread_base', models.FloatField(verbose_name='Spread base')),
                ('spread_sprint', models.FloatField(verbose_name='Spread sprint')),
                ('spread_jump', models.FloatField(verbose_name='Spread jump')),
                ('spread_downsights', models.FloatField(verbose_name='Spread downsights')),
                ('spread_standing', models.FloatField(verbose_name='Spread standing')),
                ('spread_crouching', models.FloatField(verbose_name='Spread crouching')),
                ('fire_rate_burst', models.FloatField(help_text='May be removed.', verbose_name='Fire rate (burst)')),
                ('environement_damages', models.FloatField(verbose_name='Environmental damages')),
                ('recoil_horizontal', models.FloatField(verbose_name='Recoil horizontal')),
                ('recoil_vertical', models.FloatField(verbose_name='Recoil vertical')),
                ('recoil_max_angle', models.FloatField(verbose_name='Recoil max angle')),
                ('recoil_min_angle', models.FloatField(verbose_name='Recoil min angle')),
                ('recoil_downsights', models.FloatField(verbose_name='Recoil downsights')),
                ('weapon_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='weapon', to='app.Weapon', verbose_name='Related weapon')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_heal', models.BooleanField(default=False, verbose_name='Is heal ?')),
                ('is_explosive', models.BooleanField(default=False, verbose_name='Is explosive ?')),
                ('heal', models.IntegerField(verbose_name='Heal')),
                ('shield', models.IntegerField(verbose_name='Shield')),
                ('delay', models.FloatField(verbose_name='Delay')),
                ('damages', models.IntegerField(verbose_name='Damages')),
                ('capacity', models.IntegerField(verbose_name='Capacity')),
                ('comment', models.TextField(blank=True, verbose_name='Comments')),
                ('item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='app.Item', verbose_name='Related item')),
                ('location', models.ManyToManyField(blank=True, related_name='item_detail', to='app.LocationItems', verbose_name='Location')),
            ],
        ),
    ]
