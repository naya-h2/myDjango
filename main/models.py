from django.db import models

# Create your models here.
class Lecture(models.Model):
    name = models.CharField(max_length=500, verbose_name="강의명")
    code = models.CharField(max_length=10, verbose_name="과목 코드")
    description = models.CharField(max_length=1000, verbose_name="추천 이유")

    class Meta:
        db_table = "lecture"
        verbose_name = "강의"