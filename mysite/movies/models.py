from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    audience = models.IntegerField(default=0)
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=150)
    watch_grade = models.CharField(max_length=150)
    score = models.FloatField(default=0.00)
    poster_url = models.TextField()
    description = models.TextField()

    # 원래 있던 매직 메서드를 오버라이딩 한 것
    def __str__(self):
        return f'{self.id}번째영화 - {self.title} : {self.description}'
