from django.contrib import admin
from .models import TestResult, UserAnswer


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer
    extra = 0
    fields = ('question', 'user_answer')


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'score', 'completed_at')  # Поля для отображения в списке
    list_filter = ('test', 'score', 'completed_at')  # Фильтры по тесту, баллам и дате завершения
    search_fields = ('user__username', 'test__title')  # Поиск по имени пользователя и названию теста
    ordering = ('-completed_at',)  # Сортировка по дате завершения (сначала последние)
    inlines = [UserAnswerInline]  # Включение ответов как вложенных данных
    fieldsets = (
        ('Результат', {
            'fields': ('user', 'test', 'score', 'completed_at')
        }),
    )
    readonly_fields = ('completed_at',)

    # # Запрет добавления записей
    # def has_add_permission(self, request):
    #     return False
    #
    # # Запрет изменения записей
    # def has_change_permission(self, request, obj=None):
    #     return False
