from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="churchsettings",
            name="major_event_enabled",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="churchsettings",
            name="major_event_badge",
            field=models.CharField(blank=True, default="Évènement Majeur - Église", max_length=100),
        ),
        migrations.AddField(
            model_name="churchsettings",
            name="major_event_title",
            field=models.CharField(blank=True, default="Conférence Internationale du Réveil 2026", max_length=255),
        ),
        migrations.AddField(
            model_name="churchsettings",
            name="major_event_description",
            field=models.TextField(blank=True, default="Rejoignez-nous pour un moment exceptionnel de réveil spirituel, de prière, d'adoration et d'enseignement."),
        ),
        migrations.AddField(
            model_name="churchsettings",
            name="major_event_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="churchsettings",
            name="major_event_location",
            field=models.CharField(blank=True, default="Salle de conférence de l'église", max_length=255),
        ),
        migrations.AddField(
            model_name="churchsettings",
            name="major_event_cta_label",
            field=models.CharField(blank=True, default="Rejoindre maintenant", max_length=100),
        ),
        migrations.AddField(
            model_name="churchsettings",
            name="major_event_cta_link",
            field=models.CharField(blank=True, default="/contact", max_length=255),
        ),
    ]
