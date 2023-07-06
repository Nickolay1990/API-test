from django.contrib import admin
from django.urls import path, include
from APItask.views import PostApiUpdateDeleteView, PostApiListCreateView
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth', include('rest_framework.urls')),
    path('api/v1/post/', PostApiListCreateView.as_view()),
    path('api/v1/post/<int:pk>/', PostApiUpdateDeleteView.as_view()),
]

urlpatterns += doc_urls