from django.db import models
from django.core.exceptions import ValidationError


class AboutMe(models.Model):
    image = models.ImageField(
        upload_to='about',
        verbose_name="Фото",
        help_text="Загрузите изображение, которое будет использоваться для блока 'Обо мне'."
    )
    full_name = models.CharField(
        max_length=100,
        verbose_name="ФИО",
        help_text="Введите ваше полное имя, например: Иван Иванович Иванов"
    )
    text_about_me = models.TextField(
        verbose_name="Описание",
        help_text="Расскажите немного о себе, своих увлечениях и достижениях"
    )
    experience_year = models.CharField(
        max_length=100,
        verbose_name="Опыт работы",
        help_text="Укажите ваш профессиональный опыт в годах, например: 5 лет"
    )
    students_learning = models.CharField(
        max_length=100,
        verbose_name="Обученные студенты",
        help_text="Укажите количество студентов, которых вы обучили, например: 200"
    )
    achievements = models.CharField(
        max_length=100,
        verbose_name="Достижения",
        help_text="Опишите свои достижения, например: 'Победитель конкурса преподавателей 2023'"
    )

    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"

    def clean(self):
        """
        Проверка на наличие уже существующей записи.
        """
        if not self.pk and AboutMe.objects.exists():
            raise ValidationError("Нельзя добавить более одной записи в 'Обо мне'.")

    def save(self, *args, **kwargs):
        """
        Переопределённый метод save с вызовом clean.
        """
        self.full_clean()  # Вызывает метод clean для валидации.
        super().save(*args, **kwargs)


class Contacts(models.Model):
    phone = models.CharField(
        max_length=15,
        verbose_name='Телефон',
        help_text='Введите номер телефона, например: +996555123456'
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Введите электронную почту, например: example@mail.com'
    )
    whatsapp_url = models.URLField(
        verbose_name='URL WhatsApp',
        help_text='Введите ссылку для связи через WhatsApp'
    )
    telegram_number = models.CharField(
        max_length=15,
        verbose_name='Номер Telegram',
        help_text='Введите номер телефона, связанный с Telegram, например: +996555123456'
    )
    telegram_url = models.URLField(
        verbose_name='URL Telegram',
        help_text='Введите ссылку на профиль Telegram'
    )
    instagram_account = models.CharField(
        max_length=50,
        verbose_name='Аккаунт Instagram',
        help_text='Введите имя пользователя Instagram, например: your_account'
    )
    instagram_url = models.URLField(
        verbose_name='URL Instagram',
        help_text='Введите ссылку на профиль Instagram'
    )
    telegram_bot_username = models.CharField(
        max_length=50,
        verbose_name='Имя пользователя бота',
        help_text='Введите @username вашего Telegram-бота'
    )
    telegram_bot_url = models.URLField(
        verbose_name='URL Telegram-бота',
        help_text='Введите ссылку на вашего Telegram-бота'
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f"Контакт: {self.phone} ({self.email})"

    def save(self, *args, **kwargs):
        # Ограничение на единственную запись
        if not self.pk and Contacts.objects.exists():
            raise ValidationError("Нельзя добавить более одного контакта.")
        super().save(*args, **kwargs)

