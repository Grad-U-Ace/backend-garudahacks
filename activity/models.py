from django.db import models

# Create your models here.
class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)


class Module(Activity):
    file = models.FileField(upload_to='modules')

    def __str__(self):
        return self.title



class Exercise(Activity):
    description = models.TextField()

    def __str__(self):
        return self.title

class Soal(models.Model):
    question = models.TextField()
    answer = models.TextField()
    used = models.BooleanField(default=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return self.question