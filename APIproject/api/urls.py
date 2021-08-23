from django.urls import path
from .views import article_details, article_list

urlpatterns = [
    path('articles/', article_list),
    path('articles/<int:pk>/', article_details),
]
