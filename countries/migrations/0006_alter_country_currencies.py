# Generated by Django 4.0.6 on 2022-07-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_alter_country_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='currencies',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]