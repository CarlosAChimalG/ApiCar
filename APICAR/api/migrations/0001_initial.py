7# Generated by Django 3.2.4 on 2023-10-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('idGender', models.IntegerField(db_column='idGender', primary_key=True, serialize=False)),
                ('nameGender', models.CharField(db_column='nameGender', max_length=100)),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('idProduct', models.IntegerField(db_column='idProduct', primary_key=True, serialize=False)),
                ('nameProduct', models.CharField(db_column='nameProduct', max_length=100)),
                ('priceProduct', models.FloatField(db_column='priceProduct', default=0)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('idUser', models.IntegerField(db_column='idUser', primary_key=True, serialize=False)),
                ('nameUser', models.CharField(db_column='nameUser', max_length=100)),
                ('emailUser', models.EmailField(db_column='emailUser', max_length=254, unique=True)),
                ('passwordUser', models.CharField(db_column='passwordUser', max_length=255)),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('idQuestion', models.IntegerField(db_column='idQuestion', primary_key=True, serialize=False)),
                ('nameQ', models.CharField(db_column='nameQ', max_length=100)),
                ('lastNameQ', models.CharField(db_column='lastNameQ', max_length=100)),
                ('emailQ', models.CharField(db_column='emailQ', max_length=100)),
                ('packageQ', models.CharField(db_column='packageQ', max_length=100)),
                ('personQ', models.CharField(db_column='personQ', max_length=100)),
                ('packagingQ', models.CharField(db_column='packagingQ', max_length=100)),
                ('reasonPurchaseQ', models.CharField(db_column='reasonPurchaseQ', max_length=100)),
                ('sendQ', models.CharField(db_column='sendQ', max_length=100)),
                ('markQ', models.CharField(db_column='markQ', max_length=100)),
                ('categoryQ', models.CharField(db_column='categoryQ', max_length=100)),
                ('articleQ', models.CharField(db_column='articleQ', max_length=100)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.IntegerField(db_column='idRol', primary_key=True, serialize=False)),
                ('nameRol', models.CharField(db_column='nameRol', max_length=100)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
    ]
