# Generated by Django 5.0.2 on 2024-03-12 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrot_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='fecha_de_incio',
            new_name='fecha_de_inicio',
        ),
        migrations.AlterField(
            model_name='cursos',
            name='fecha_de_finalizacion',
            field=models.DateField(),
        ),
    ]
