from django.contrib import admin
from .models import TestModel, QuestionModel


class QuestionInline(admin.StackedInline):
    model = QuestionModel
    extra = 1
    fields = ('title', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option')
    readonly_fields = ('created_at', 'updated_at')


class TestModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    fieldsets = (
        ("Тест", {
            'fields': ('title', 'description','created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    inlines = [QuestionInline]
    readonly_fields = ('created_at', 'updated_at')


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'test', 'correct_option', 'created_at', 'updated_at')
    search_fields = ('title', 'option_a', 'option_b', 'option_c', 'option_d')
    list_filter = ('test', 'created_at')
    ordering = ('-created_at',)
    fieldsets = (
        ("Вопрос", {
            'fields': ('test', 'title')
        }),
        ('Варианты', {
            'fields': ('option_a', 'option_b', 'option_c', 'option_d'),
        }),
        ('Правильный ответ', {
            'fields': ('correct_option',),
            'classes': ('collapse',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(TestModel, TestModelAdmin)
admin.site.register(QuestionModel, QuestionModelAdmin)
