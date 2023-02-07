from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=120)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='task')
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

