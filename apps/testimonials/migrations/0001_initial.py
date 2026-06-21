from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                ("id",         models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("name",       models.CharField(max_length=150)),
                ("text",       models.TextField()),
                ("image",      models.ImageField(blank=True, null=True, upload_to="testimonials/")),
                ("order",      models.PositiveIntegerField(default=0)),
                ("is_active",  models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["order", "-created_at"]},
        ),
    ]
