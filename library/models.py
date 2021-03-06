from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, MaxValueValidator


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(TimestampedModel):

    title = models.CharField(max_length=200, db_index=True,
                             validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
                             ])
    author = models.CharField(max_length=50)
    score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
        ], blank=True)
    link = models.URLField(blank=True)
    content = models.TextField()
    photo = models.ImageField(blank=True)
