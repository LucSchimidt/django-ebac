from django.db import models
from blog.models import post


class Comment(models.Model):
    post = models.ForeignKey(post.Postagem, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Commented {self.body} by {self.name}'