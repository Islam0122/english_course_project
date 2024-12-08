# Generated by Django 5.1.3 on 2024-12-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Выберите изображение для категории', upload_to='images/', verbose_name='Изображение')),
                ('title', models.CharField(help_text='Введите название категории (до 100 символов)', max_length=100, verbose_name='Название категории')),
                ('description', models.TextField(help_text='Добавьте описание категории', verbose_name='Описание категории')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Автоматически добавляется дата создания', verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название уровня (до 100 символов)', max_length=100, verbose_name='Название уровня')),
                ('image', models.ImageField(help_text='Выберите изображение для уровня', upload_to='images/', verbose_name='Изображение уровня')),
                ('description', models.TextField(help_text='Добавьте описание уровня', verbose_name='Описание уровня')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Автоматически добавляется дата создания', verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Уровень',
                'verbose_name_plural': 'Уровни',
                'ordering': ['-created_at'],
            },
        ),
    ]