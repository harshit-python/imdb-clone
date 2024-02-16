from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    # validators
    # field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("name is too short!")
        else:
            return value

    # object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description cannot be same!")
        else:
            return data

