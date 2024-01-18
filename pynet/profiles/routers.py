from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from message import views

schema_view = get_schema_view(
   openapi.Info(
      title="PyNet API",
      default_version='v1',
      description="Docs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('wall/', include('wall.urls')),
    path('feed/', include('feed.urls')),
    path('follower/', include('followers.urls')),
    path('', include('profiles.urls')),
    path('message/', include([
        path('create/', (views.CreateDialogView.as_view()), name='create_dialog'),
        path('<chat_id>/', (views.MessagesView.as_view()), name='messages'),
    ])),
]
