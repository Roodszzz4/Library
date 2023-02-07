from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    task = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = 'Задачи'



