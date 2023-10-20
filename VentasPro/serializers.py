from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MytokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['grupo_id'] = user.groups.first().id if user.groups.exists() else None

        return token