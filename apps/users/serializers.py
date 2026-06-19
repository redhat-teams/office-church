from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ["id", "username", "email", "first_name", "last_name",
                  "role", "phone", "avatar", "is_active", "date_joined"]
        read_only_fields = ["id", "date_joined"]

class UserCreateSerializer(serializers.ModelSerializer):
    """Création d'un utilisateur depuis l'admin (avec mot de passe)."""
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model  = User
        fields = ["id", "username", "email", "first_name", "last_name",
                  "phone", "role", "is_active", "password"]
        read_only_fields = ["id"]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà utilisé.")
        return value

    def validate_email(self, value):
        if value and User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cette adresse e-mail est déjà utilisée.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ["first_name", "last_name", "email", "phone", "role", "is_active"]
