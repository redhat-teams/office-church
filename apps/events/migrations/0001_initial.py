from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id",          models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("title",       models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("date",        models.DateField()),
                ("time",        models.TimeField(blank=True, null=True)),
                ("location",    models.CharField(blank=True, max_length=255)),
                ("category",    models.CharField(choices=[("culte","Culte"),("conference","Conférence"),("formation","Formation"),("evangelisation","Évangélisation"),("jeunesse","Jeunesse"),("priere","Prière"),("autre","Autre")], default="culte", max_length=30)),
                ("image",       models.ImageField(blank=True, null=True, upload_to="events/")),
                ("created_at",  models.DateTimeField(auto_now_add=True)),
                ("updated_at",  models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["date"]},
        ),
    ]
