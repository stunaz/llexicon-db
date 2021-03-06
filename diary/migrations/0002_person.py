# Generated by Django 2.2.10 on 2020-04-05 00:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(related_name='people', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
                'ordering': ('name',),
            },
        ),
    ]
