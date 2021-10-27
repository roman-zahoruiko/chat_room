from django.db import models


class Messages(models.Model):
    author_username = models.CharField(unique=True, blank=True, max_length=20)
    author_email = models.EmailField(unique=True, blank=False)
    text = models.TextField(blank=False, max_length=99)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author_username}, {self.author_email}, {self.created}, {self.text[:20]}"

    class Meta:
        ordering = ("-created",)
