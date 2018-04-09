from rest_framework import serializers
from apis.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'company',
                  'age', 'city', 'state', 'pin', 'email', 'web')
