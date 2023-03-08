from rest_framework import serializers
from .models import Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    queryset = Track.objects.all()
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'number', 'tracks']

    def validate(self, data):
        if len(data['tracks']) != data['number']:
            raise serializers.ValidationError("number must be equal")
        return data

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album
