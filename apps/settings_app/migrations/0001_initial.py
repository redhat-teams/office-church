from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="ChurchSettings",
            fields=[
                ("id",         models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("name",       models.CharField(default="Mon Église", max_length=255)),
                ("tagline",    models.CharField(blank=True, max_length=255)),
                ("email",      models.EmailField(blank=True)),
                ("phone",      models.CharField(blank=True, max_length=30)),
                ("address",    models.CharField(blank=True, max_length=255)),
                ("facebook",   models.URLField(blank=True)),
                ("youtube",    models.URLField(blank=True)),
                ("instagram",  models.URLField(blank=True)),
                ("whatsapp",   models.CharField(blank=True, max_length=30)),
                ("logo",       models.ImageField(blank=True, null=True, upload_to="settings/")),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Paramètres de l'église"},
        ),
    ]
