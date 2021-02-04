# Generated by Django 3.1.4 on 2021-02-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210203_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=1, max_length=50)),
                ('answer', models.CharField(default=1, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='score2',
            fields=[
                ('score2', models.IntegerField(default=1)),
                ('username', models.CharField(default=1, max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]