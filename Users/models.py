from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile-photos/', blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' (' + str(self.bio) + ')'
