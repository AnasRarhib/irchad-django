# Generated by Django 4.1.2 on 2023-04-26 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accueil", "0006_alter_message_cv_alter_message_session"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="session",
            field=models.ManyToManyField(to="accueil.sessioncv"),
        ),
    ]
