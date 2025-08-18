from rest_framework import serializers

from users.models import Profession

class ProfessionListSerializer(serializers.ModelSerializer):
    model = Profession
