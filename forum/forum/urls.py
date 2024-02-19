
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from api import views

router = routers.SimpleRouter()
router.register(r'subjectlist', views.SubjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subject/', include('main_page.urls'), name='subject'),
    path('account/', include('account.urls'), name='account'),
    path('api/v1/', include(router.urls), name='api'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    