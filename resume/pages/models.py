from django.db import models


class Post(models.Model):
    title = models.CharField(
        verbose_name='Заголовок поста',
        help_text='Введите заголовок',
        max_length=128,
    )
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите текст',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

