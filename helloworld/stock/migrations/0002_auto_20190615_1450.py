# Generated by Django 2.2.1 on 2019-06-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_glass', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('quntity', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Travel',
        ),
    ]