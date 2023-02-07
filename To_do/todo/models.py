from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='task')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

