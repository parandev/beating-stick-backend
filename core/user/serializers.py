from core.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, source='public_id', format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model=User
        fields=[ 'id', 'first_name', 'last_name', 'username', 'email', 'bio', 'avatar', 'is_active', 'created', 'updated']
        read_only_field=['is_active']
