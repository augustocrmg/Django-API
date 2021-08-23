from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
#article_details, article_list

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(router.urls)),
    #path('articles/', ArticleList.as_view()),
    #path('articles/<int:id>/', ArticleDetails.as_view()),
    #path('articles/', article_list),
    #path('articles/<int:pk>/', article_details),
]
