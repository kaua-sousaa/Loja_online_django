from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from app_pratas import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tela_inicio, name="tela_inicio"),
    path('cadastrar/', views.cad_item, name="cadastrar_item"),
    path('excluir/', views.excluir_item, name="excluir_item"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
