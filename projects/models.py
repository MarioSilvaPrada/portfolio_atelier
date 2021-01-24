from django.db import models


class Project(models.Model):
    # many-to-one relationship
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
