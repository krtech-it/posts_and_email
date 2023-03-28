from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Основной текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Автор")
    likes = models.PositiveIntegerField("Отметки нравится", default=0)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return F"{self.title} by {self.author}"

    class Meta:
        verbose_name_plural = "Записи"
        verbose_name = "Запись"

# Create your models here.
