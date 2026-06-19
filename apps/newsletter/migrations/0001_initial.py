from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="NewsletterSubscriber",
            fields=[
                ("id",         models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("email",      models.EmailField(unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_active",  models.BooleanField(default=True)),
            ],
        ),
    ]
