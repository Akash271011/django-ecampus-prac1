# Generated by Django 4.0.2 on 2022-02-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=50)),
                ('eage', models.IntegerField()),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.IntegerField()),
            ],
            options={
                'db_table': 'employee1',
            },
        ),
    ]
