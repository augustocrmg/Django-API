from django.urls import path
from .views import ArticleDetails, ArticleList
#article_details, article_list

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view()),
    #path('articles/', article_list),
    #path('articles/<int:pk>/', article_details),
]
