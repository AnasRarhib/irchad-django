# Generated by Django 4.1.2 on 2023-04-26 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accueil", "0004_cv_sessioncv_remove_userr_sexe_userr_traitementcv_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="contenu",
            field=models.CharField(max_length=16383),
        ),
    ]