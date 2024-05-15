from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import News, Comment
from .forms import CommentForm


def news_feed(request):
    news_list = News.objects.all()
    return render(request, 'core/news_feed.html', {'news_list': news_list})


@login_required
@require_POST
def add_comment(request, news_id):
    news = get_object_or_404(News, id=news_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.news = news
        comment.user = request.user
        comment.save()
    return redirect('news_feed')


def pricing(request):
    return render(request, 'core/subscriptions.html')
