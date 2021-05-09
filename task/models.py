from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=50)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['complete']

    def __str__(self):
        return self.title
