from django.db import models
from django.contrib.auth.models import User

#Model for topics of posts.

TYPE = (
    (0,'News'),
    (1,'Opinion'),
    (2, 'Mail')
)

class Topics(models.Model):
    title = models.CharField(max_length=200, unique=True)
    type = models.IntegerField(choices=TYPE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title