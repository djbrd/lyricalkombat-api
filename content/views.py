from rest_framework import generics
from rest_framework.decorators import api_view
from content.models import Prompt, Artist, KeyPhrase
from content.serializers import PromptSerializer, ArtistSerializer, KeyPhraseSerializer, SubPromptSerializer
import random
from django.http import JsonResponse

class PromptList(generics.ListCreateAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    name = 'prompt-list'


class PromptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    name = 'prompt-detail'


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-list'


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-detail'


class KeyphraseList(generics.ListCreateAPIView):
    queryset = KeyPhrase.objects.all()
    serializer_class = KeyPhraseSerializer
    name = 'keyphrase-list'


class KeyphraseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeyPhrase.objects.all()
    serializer_class = KeyPhraseSerializer
    name = 'keyphrase-detail'

@api_view(['GET'])
def random_subprompt(request):
    if request.method == 'GET':
        prompts = Prompt.objects.all()
        prompt = random.choice(prompts)
        prompt_serializer = SubPromptSerializer(prompt)
        return JsonResponse(prompt_serializer.data)

