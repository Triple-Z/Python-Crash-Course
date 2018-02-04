from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' ' + self.date_added + '\n\n' + self.text