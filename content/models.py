from django.db import models
from django.contrib.postgres.fields import ArrayField


class Artist(models.Model):
    name = models.CharField(max_length=128, unique=True)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class KeyPhrase(models.Model):
    sponsor = models.CharField(max_length=128)
    phrase = models.CharField(max_length=256)
    class Meta:
        ordering = ('sponsor',)
        unique_together = ('sponsor', 'phrase')

    def __str__(self):
        return self.sponsor + ', ' + self.phrase


class Prompt(models.Model):
    title = models.CharField(max_length=256, unique=True, default='')
    video_id = models.CharField(max_length=11, default='')
    start = models.PositiveSmallIntegerField(default=0)
    end = models.PositiveSmallIntegerField(default=0)
    keywords = models.CharField(max_length=256, default='')
    artists = models.ManyToManyField(
        Artist,
        related_name='prompts',
        related_query_name='prompt',
    )
    keyphrase = models.ForeignKey(KeyPhrase, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title