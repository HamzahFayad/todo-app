from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_photo = models.ImageField(upload_to='task_photos/', blank=True, null=True)
    text = models.CharField(max_length=200)
    date_published = models.DateTimeField(blank=True,
                                          default=date.today,
                                          )
    # user = models.ForeignKey(User,
    #                         on_delete=models.CASCADE,
    #                         related_name='users',
    #                         related_query_name='user',
    #                         )

    class Meta:
        ordering = ['date_published']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def get_photo_url(self):
        if self.task_photo and hasattr(self.task_photo, 'url'):
            return self.task_photo.url
        else:
            return "/static/img/white.png"

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text + ' / ' + self.date_published
