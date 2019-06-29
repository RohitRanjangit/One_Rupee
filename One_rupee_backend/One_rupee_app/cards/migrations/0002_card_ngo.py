# Generated by Django 2.2.1 on 2019-06-28 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ngo', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='ngo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo.Ngo', verbose_name='connected_ngo'),
        ),
    ]