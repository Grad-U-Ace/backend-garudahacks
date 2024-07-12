from django.db import models


# Create your models here.
class Mapel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)
    mapel = models.ForeignKey(Mapel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    ACTIVITY_TYPES = (
        ('modul', 'Modul'),
        ('exercise', 'Exercise'),
    )
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    topic = models.ForeignKey('Topic', related_name='activities', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=ACTIVITY_TYPES)

    def __str__(self):
        return self.title


class Modul(Activity):
    file = models.FileField(upload_to='modules')

    def save(self, *args, **kwargs):
        self.type = 'modul'
        super().save(*args, **kwargs)

class Exercise(Activity):
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.type = 'exercise'
        super().save(*args, **kwargs)

class Soal(models.Model):
    question = models.TextField()
    answer = models.TextField()
    used = models.BooleanField(default=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return self.question