from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/<int:topic_id>/', views.topic_news, name='topic_news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]
