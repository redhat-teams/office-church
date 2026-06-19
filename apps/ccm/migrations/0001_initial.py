from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="CCMContent",
            fields=[
                ("id",          models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("title",       models.CharField(max_length=255)),
                ("subtitle",    models.CharField(blank=True, max_length=255)),
                ("description", models.TextField(blank=True)),
                ("image",       models.ImageField(blank=True, null=True, upload_to="ccm/")),
                ("video_url",   models.URLField(blank=True)),
                ("order",       models.PositiveIntegerField(default=0)),
                ("is_active",   models.BooleanField(default=True)),
                ("created_at",  models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["order"]},
        ),
    ]
