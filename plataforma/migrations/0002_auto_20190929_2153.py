# Generated by Django 2.2.4 on 2019-09-29 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Imagem',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_Main_Img',
            new_name='arquivo',
        ),
    ]
