from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/about_me/', include('app.main.urls')),
                  path('api/v1/lessons/', include('app.Lesson.urls')),
                  path('api/v1/', include('app.english_test.urls')),
                  path('api/v1/', include('app.testresult.urls')),

              ] + urls_swagger
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
