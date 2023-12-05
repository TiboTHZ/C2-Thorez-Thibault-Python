# Generated by Django 4.2.8 on 2023-12-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('auteur', models.CharField(max_length=255)),
                ('date_publication', models.DateField()),
                ('note', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
