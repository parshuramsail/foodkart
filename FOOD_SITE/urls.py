from django.contrib import admin
from django.urls import path, include
from users import views

from django.conf.urls.static import static
from django.conf import Settings, settings

from django.contrib.auth import views as authentication_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),

    # users views
    path('register/', views.register, name='register'),
    path('login/', authentication_view.LoginView.as_view(
        template_name="users/login.html"), name='login'),
    path('logout/', authentication_view.LogoutView.as_view(
        template_name="users/logout.html"), name='logout'),
    path('profile/', views.profilepage, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
