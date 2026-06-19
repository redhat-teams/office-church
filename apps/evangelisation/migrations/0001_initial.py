from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="EvangelisationRegistration",
            fields=[
                ("id",         models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name",  models.CharField(max_length=100)),
                ("email",      models.EmailField(blank=True)),
                ("phone",      models.CharField(max_length=30)),
                ("city",       models.CharField(blank=True, max_length=100)),
                ("message",    models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
