from django.db import models


class GitRepo(models.Model):
    name = models.CharField(max_length=200)
    _id = models.IntegerField(default=0)
    lang = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
