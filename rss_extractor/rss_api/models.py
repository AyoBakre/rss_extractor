# rss_api/models.py
from django.db import models


class ParsedData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    last_parsed = models.DateTimeField(auto_now=True)
