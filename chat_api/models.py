from django.db import models


class Messages(models.Model):
    author = models.CharField(unique=True, blank=False, max_length=100)
    author_email = models.EmailField(unique=True, blank=False)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}, {self.author_email}, {self.created}, {self.text[:20]}"

    class Meta:
        ordering = ("-created",)

    def get_messages_pagination(self, start, end):  # Using DRF Pagination out of the task
        return Messages.objects.order_by("-created").all()[start:end]

    def get_message_by_id(self, message_id):
        message = Messages.objects.get(pk=message_id)
        if not message:
            return None
        else:
            return message


