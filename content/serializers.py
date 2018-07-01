from rest_framework import serializers
from content.models import Prompt, Artist, KeyPhrase


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'name',
        )


class KeyPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPhrase
        fields = (
            'sponsor',
            'phrase'
        )


class KeyPhrasePrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return instance.sponsor + ', ' + instance.phrase


class PromptSerializer(serializers.ModelSerializer):
    artists = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Artist.objects.all()
    )

    keyphrase = KeyPhrasePrimaryKeyRelatedField(
        queryset=KeyPhrase.objects.all()
    )

    class Meta:
        model = Prompt
        fields = "__all__"


class SubPromptSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True, read_only=True)
    keyphrase = KeyPhraseSerializer(read_only=True)

    class Meta:
        model = Prompt
        fields = ('id',
                  'title',
                  'artists',
                  'video_id',
                  'start',
                  'end',
                  'keywords',
                  'keyphrase')