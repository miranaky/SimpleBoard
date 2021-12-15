from rest_framework.serializers import CharField, ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.get("password")
        new_user = super().create(validated_data)
        new_user.set_password(password)
        new_user.save()
        return new_user
