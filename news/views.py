from .models import Article

from django.shortcuts import get_object_or_404, render


def index(request):
    articles = Article.objects.order_by('-pub_date')
    top3_articles = Article.objects.order_by('-pub_date')[:3]
    top10_articles = Article.objects.order_by('-pageviews')[:10]

    context = {
        'articles': articles,
        'top3_articles': top3_articles,
        'top10_articles': top10_articles,
    }
    return render(request, "home.html", context)


def detail(request, article_id):
    try:
        article = get_object_or_404(Article, pk=article_id)
        article.pageviews += 1
        article.save(update_fields=['pageviews'])

    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'news/detail.html', {'article': article})
