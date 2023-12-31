# Generated by Django 4.1.2 on 2023-04-26 22:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accueil", "0003_userr_userr"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cv",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Date de creation",
                    ),
                ),
                ("file", models.FileField(upload_to="file/")),
                ("fileID", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="SessionCV",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Date de creation",
                    ),
                ),
                ("etat", models.IntegerField(default=0)),
                ("cvUploaded", models.BooleanField(default=False)),
                ("accepted", models.BooleanField(default=False)),
                ("usernameRh", models.CharField(max_length=20)),
                ("usernameUser", models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(model_name="userr", name="sexe",),
        migrations.AddField(
            model_name="userr",
            name="traitementCV",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userr",
            name="username",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Date de d'envoi",
                    ),
                ),
                ("contenu", models.CharField(max_length=100000)),
                ("username", models.CharField(max_length=20)),
                ("cv", models.ManyToManyField(to="accueil.cv")),
                ("session", models.ManyToManyField(to="accueil.sessioncv")),
            ],
        ),
    ]
