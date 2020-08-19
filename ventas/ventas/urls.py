from django.contrib import admin
from django.urls import path,include

#para imagenes
from django.conf import settings
from django.conf.urls.static import static
#para login y logout
from django.contrib.auth import views as auth_views
#para registrar
from usuarios import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('producto.urls'),name='producto'),

    path('registrar/', user_views.registrar, name='registrar'),    
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
