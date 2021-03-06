# Generated by Django 2.2.1 on 2019-07-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('category', models.CharField(choices=[('AGC', 'Age care (care for the aged/Older persons)'), ('AGR', 'Agriculture'), ('AW', 'Animal Welfare'), ('ANC', 'Art & Craft'), ('CE', 'Child Education'), ('CUD', 'Cities/Urban Development'), ('CD', 'Community Development'), ('CNH', ' Culture & Heritage'), ('D', 'Disability'), ('DM', 'Disaster Management'), ('EDU', 'Education'), ('ENVI', 'Environmental issues'), ('HNH', 'Health & Hygiene'), ('HA', ' HIV/AIDS'), ('HS', 'Housing & Slums'), ('P', 'Population'), ('PR', 'Poverty Removal'), ('RD', 'Rural Development'), ('STD', 'Science & Technology Development'), ('TP', 'Tribal people'), ('WM', 'Waste Management'), ('DW', 'Drinking Water'), ('WO', 'Women'), ('O', 'others')], max_length=50, verbose_name='category')),
                ('shortDescription', models.TextField(verbose_name='shortDescription')),
                ('longDescription', models.TextField(verbose_name='longDescription')),
                ('amount_requested', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='amount_requested')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]
