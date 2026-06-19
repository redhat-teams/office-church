import uuid
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from .cinetpay import create_cinetpay_payment

@api_view(["POST"])
@permission_classes([AllowAny])
def create_cinetpay_checkout(request):
    serializer = PaymentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    transaction_id = str(uuid.uuid4())
    payment = Payment.objects.create(
        transaction_id=transaction_id,
        amount=serializer.validated_data["amount"],
        customer_email=serializer.validated_data["email"],
        provider="cinetpay",
    )

    payload = {
        "apikey":         settings.CINETPAY_API_KEY,
        "site_id":        settings.CINETPAY_SITE_ID,
        "transaction_id": transaction_id,
        "amount":         str(payment.amount),
        "currency":       "XOF",
        "description":    "Donation Church Platform",
        "notify_url":     f"{settings.BACKEND_URL}/api/cinepay/cinetpay/webhook/",
        "return_url":     f"{settings.FRONTEND_URL}/payment-success",
    }

    result = create_cinetpay_payment(payload)
    return Response(result)

@api_view(["POST"])
@permission_classes([AllowAny])
def cinetpay_webhook(request):
    transaction_id = request.data.get("transaction_id")
    try:
        payment = Payment.objects.get(transaction_id=transaction_id)
        payment.status = "paid"
        payment.save()
    except Payment.DoesNotExist:
        pass
    return Response({"success": True})
