# Generated by Django 3.1.4 on 2021-02-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210203_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score1',
            name='id',
        ),
        migrations.AlterField(
            model_name='score1',
            name='username',
            field=models.CharField(default=1, max_length=50, primary_key=True, serialize=False),
        ),
    ]