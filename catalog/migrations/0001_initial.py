# Generated by Django 2.1.5 on 2019-03-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaTourHoleModel',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('par', models.IntegerField(blank=True, null=True)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('meters', models.IntegerField(blank=True, null=True)),
                ('CTP', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
                ('LD', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
                ('tussle', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
