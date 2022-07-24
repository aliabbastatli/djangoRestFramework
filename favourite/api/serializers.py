from rest_framework import serializers

from favourite.models import Favourite


class FavoriteListCreateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

    def validate(self, attrs):
        queryset = Favourite.objects.filter(post=attrs["post"], user=attrs["user"])

        if queryset.exists():  # favorillere eklendiyse bi daha eklenmesin.
            raise serializers.ValidationError("Already added to favorites!")
        return attrs


class FavoriteAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
