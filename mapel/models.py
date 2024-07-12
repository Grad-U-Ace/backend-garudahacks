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
    title = models.CharField(max_length=100)
    topic = models.ForeignKey('Topic', related_name='activities', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('modul', 'Modul'), ('exercise', 'Exercise')])

    def __str__(self):
        return self.title


class Modul(Activity):
    file = models.FileField(upload_to='modules', null=True, blank=True)
    content_suggestion = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.type = 'modul'
        super().save(*args, **kwargs)


class Exercise(Activity):
    description = models.TextField()

    class Meta:
        proxy = False

    def save(self, *args, **kwargs):
        self.type = 'exercise'
        super().save(*args, **kwargs)


class Soal(models.Model):
    question = models.TextField()
    answer = models.TextField()
    used = models.BooleanField(default=False)
    exercise = models.ForeignKey(Exercise, related_name='soal_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.question

