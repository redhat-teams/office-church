from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Teaching",
            fields=[
                ("id",          models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("title",       models.CharField(max_length=255)),
                ("speaker",     models.CharField(max_length=150)),
                ("description", models.TextField(blank=True)),
                ("date",        models.DateField()),
                ("category",    models.CharField(choices=[("enseignement","Enseignement"),("predication","Prédication"),("etude_biblique","Étude biblique"),("temoignage","Témoignage"),("autre","Autre")], default="enseignement", max_length=30)),
                ("video_url",   models.URLField(blank=True)),
                ("audio_url",   models.URLField(blank=True)),
                ("thumbnail",   models.ImageField(blank=True, null=True, upload_to="teachings/")),
                ("created_at",  models.DateTimeField(auto_now_add=True)),
                ("updated_at",  models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-date"]},
        ),
    ]
