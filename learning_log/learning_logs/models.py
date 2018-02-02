from django.db import models


class Topic(models.Model):
    """User learning topic"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Use string to present """
        return self.text


class Entry(models.Model):
    """Learning specific knowledge"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # 18-2
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text