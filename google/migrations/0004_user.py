# Generated by Django 2.1.7 on 2019-04-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0003_auto_20190402_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
