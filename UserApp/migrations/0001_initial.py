# Generated by Django 4.1.4 on 2022-12-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
    ]
