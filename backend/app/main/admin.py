from django.contrib import admin
from django.utils.html import format_html
from .models import AboutMe , Contacts


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "experience_year", "students_learning",)
    fieldsets = (
        ("Основная информация", {
            "fields": ("image_","image", "full_name", "text_about_me")
        }),
        ("Детали", {
            "fields": ("experience_year", "students_learning", "achievements")
        }),
    )
    ordering = ("-experience_year",)
    empty_value_display = "-пусто-"
    readonly_fields = ("image_",)

    def image_(self, obj):
        """
        Отображение изображения в админке.
        """
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "Нет изображения"

    image_.short_description = "Превью изображения"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return AboutMe.objects.exists()


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    # Поля, которые отображаются в списке моделей
    list_display = (
        "phone",
        "email",
        "whatsapp_url",
        "telegram_number",
        "telegram_url",
        "instagram_account",
        "instagram_url",
        "telegram_bot_username",
        "telegram_bot_url",
    )

    def has_add_permission(self, request):
        """
        Разрешаем добавление, только если записи еще нет.
        """
        return not Contacts.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """
        Запрещаем удаление записей.
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Разрешаем изменение только если запись существует.
        """
        return Contacts.objects.exists()

