from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # excluding this as we are passing its pk in the url
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'

    # reviews = ReviewSerializer(many=True, read_only=True)
    reviews = serializers.StringRelatedField(many=True, read_only=True)

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


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'

    # this will map all the related watchlist object inside stream platform object
    # always use related_name from model foreign key

    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)
