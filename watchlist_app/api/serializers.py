from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = '__all__'

    def create(self, validated_data):
        return StreamPlatform.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website', instance.website)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance


class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'

    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance

    # validators
    # field level validation
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("title is too short!")
        else:
            return value

    # object level validation
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("title and description cannot be same!")
        else:
            return data
