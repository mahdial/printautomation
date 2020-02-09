from django.contrib.auth.models import User
from django.db import models

class ProfileDetail(models.Model):
    tell = models.CharField(max_length=150)
    birthday = models.DateTimeField(auto_now_add=False)

    img = models.ImageField(default='default.png', blank=True)
    madarek1 = models.ImageField(default='default.png', blank=True)
    madarek2 = models.ImageField(default='default.png', blank=True)
    madarek3 = models.ImageField(default='default.png', blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='ProfileDetail2User')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
