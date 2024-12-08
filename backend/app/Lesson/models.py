from django.db import models


class Category(models.Model):
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение',
        help_text='Выберите изображение для категории'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название категории',
        help_text='Введите название категории (до 100 символов)'
    )
    description = models.TextField(
        verbose_name='Описание категории',
        help_text='Добавьте описание категории'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Автоматически добавляется дата создания'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']  # Сортировка по дате создания (новые первыми)


class Level(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название уровня',
        help_text='Введите название уровня (до 100 символов)'
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение уровня',
        help_text='Выберите изображение для уровня'
    )
    description = models.TextField(
        verbose_name='Описание уровня',
        help_text='Добавьте описание уровня'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Автоматически добавляется дата создания'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'
        ordering = ['-created_at']  # Сортировка по дате создания (новые первыми)


