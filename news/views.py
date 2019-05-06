from .models import Article

from django.shortcuts import get_object_or_404, render


def index(request):
    articles = Article.objects.order_by('-pub_date')[:5]
    context = {
        'articles': articles,
    }
    return render(request, "home.html", context)

def detail(request, article_id):
    try:
        article = get_object_or_404(Article, pk=article_id)
        article.increase_views
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'news/detail.html', {'article': article})
