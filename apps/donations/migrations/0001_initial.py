from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Donation",
            fields=[
                ("id",             models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("donor_name",     models.CharField(blank=True, max_length=150)),
                ("email",          models.EmailField(blank=True)),
                ("phone",          models.CharField(blank=True, max_length=30)),
                ("amount",         models.DecimalField(decimal_places=2, max_digits=12)),
                ("currency",       models.CharField(default="FCFA", max_length=10)),
                ("payment_method", models.CharField(choices=[("wave","Wave"),("orange_money","Orange Money"),("cinetpay","CinetPay"),("paypal","PayPal"),("cash","Espèces"),("other","Autre")], default="wave", max_length=20)),
                ("status",         models.CharField(choices=[("pending","En attente"),("completed","Validé"),("failed","Échoué"),("refunded","Remboursé")], default="pending", max_length=20)),
                ("message",        models.TextField(blank=True)),
                ("transaction_id", models.CharField(blank=True, max_length=150)),
                ("created_at",     models.DateTimeField(auto_now_add=True)),
                ("updated_at",     models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
