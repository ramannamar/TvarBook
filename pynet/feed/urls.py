from django.urls import path
from . import views
from djoser.views import TokenCreateView

urlpatterns = [
    path('<int:pk>', views.FeedView.as_view({'get': 'retrieve'})),
    path('', views.FeedView.as_view({'get': 'list'})),
]
