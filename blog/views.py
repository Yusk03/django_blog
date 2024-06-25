from django.shortcuts import render, get_object_or_404
from .models import Topic, News


def home(request):
    topics = Topic.objects.all()
    news = News.objects.all().order_by('-date_published')
    return render(request, 'blog/home.html', {'topics': topics, 'news': news})


def topic_news(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    news = News.objects.filter(topic=topic).order_by('-date_published')
    return render(request, 'blog/topic_news.html', {'topic': topic, 'news': news})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'blog/news_detail.html', {'news_item': news_item})
