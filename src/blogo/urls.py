from django.urls import path
from .views import index, articles

urlpatterns = [
    path('', index, name="blog-index"),
    path('articles-<str:numero_article>/', articles, name="blog-articles"),
]