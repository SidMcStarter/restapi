# Generated by Django 4.0.6 on 2022-07-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_country_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterField(
            model_name='country',
            name='currencies',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='languages',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
