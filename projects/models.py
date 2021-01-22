from django.db import models



class Project(models.Model):

    author = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.author
