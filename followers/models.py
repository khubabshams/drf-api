from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to 'owner' and 'post'.
    'owner' and 'followed are a User instances.
    'unique_together' makes sure a user can't follow the same user twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.followed}'
