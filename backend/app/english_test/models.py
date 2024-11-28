from django.db import models


class TestModel(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название теста',  # Название поля на русском
        help_text='Укажите название теста, которое будет отображаться в интерфейсе.'  # Описание поля на русском
    )
    description = models.TextField(
        verbose_name='Описание теста',
        help_text='Напишите описание теста, которое будет видно пользователю.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата и время, когда тест был создан.'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
        help_text='Дата и время последнего обновления теста.'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class QuestionModel(models.Model):
    test = models.ForeignKey(
        TestModel,
        related_name='questions',
        on_delete=models.CASCADE,
        verbose_name='Тест',
        help_text='Выберите тест, к которому относится этот вопрос.'
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Вопрос',
        help_text='Введите текст вопроса.'
    )
    option_a = models.TextField(
        verbose_name='Вариант A',
        help_text='Введите текст для варианта A.'
    )
    option_b = models.TextField(
        verbose_name='Вариант B',
        help_text='Введите текст для варианта B.'
    )
    option_c = models.TextField(
        verbose_name='Вариант C',
        help_text='Введите текст для варианта C.'
    )
    option_d = models.TextField(
        verbose_name='Вариант D',
        help_text='Введите текст для варианта D.'
    )
    correct_option = models.CharField(
        max_length=1,
        choices=[('A', 'Вариант A'), ('B', 'Вариант B'), ('C', 'Вариант C'), ('D', 'Вариант D')],
        verbose_name='Правильный вариант',
        help_text='Выберите правильный вариант ответа (A, B, C или D).'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата и время, когда вопрос был создан.'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
        help_text='Дата и время последнего обновления вопроса.'
    )
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
