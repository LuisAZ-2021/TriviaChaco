# Generated by Django 3.2.6 on 2021-08-19 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz1', '0002_preguntasrespondidas_quizusuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntasrespondidas',
            old_name='usuario',
            new_name='quizUser',
        ),
    ]
