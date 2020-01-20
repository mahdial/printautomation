from django.contrib.auth.models import User
from django.db import models

class ProfileDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
