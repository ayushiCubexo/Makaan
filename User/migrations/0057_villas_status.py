# Generated by Django 4.1.1 on 2022-10-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0056_alter_apartments_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='villas',
            name='status',
            field=models.CharField(default='Fresh', max_length=50),
        ),
    ]