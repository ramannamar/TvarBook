from django.contrib import admin
from django.urls import path, include
from djoser.views import TokenCreateView

from profiles.views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('auth/token/', TokenCreateView.as_view(), name='token_create'),

    path('api/v1/', include('profiles.routers')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

