# Generated by Django 2.1.7 on 2019-04-02 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('google', '0002_auto_20190402_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('url', models.URLField(unique=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='google.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='google.Webpage'),
        ),
    ]