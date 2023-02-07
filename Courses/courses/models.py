from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=55)
    photo = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name




class Course(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return self.title





class Subject(models.Model):
    name = models.CharField(max_length=55)
    course = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name

    def course_display(self):
        return ', '.join([course.title for course in self.course.all()])
    course_display.short_description = 'Course'




