# Generated by Django 2.0 on 2019-05-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_auto_20190522_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='aritcle',
            name='star',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
