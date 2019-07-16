from .models import Article
import pdb

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

def head(request):
    top3_articles = Article.objects.order_by('-pub_date')[:3]

    context = {
        'top3_articles': top3_articles,
    }
    return render(request, "head.html", context)


def detail(request, article_id):
    try:
        article = get_object_or_404(Article, pk=article_id)
        article.pageviews += 1
        article.save(update_fields=['pageviews'])

        top3_articles = Article.objects.order_by('-pub_date')[:3]

        recommend_articles = recommendArticles(request, article)

        context = {
            'top3_articles': top3_articles,
            'recommend_articles': recommend_articles,
        }

    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'news/detail.html', {'article': article, 'recommend_articles': recommend_articles} )

def recommendArticles(request, article):
    r_articles = Article.objects.order_by('-pub_date')[:100]

    r_articles_result = []
    num = 0
    for r_article in r_articles:
        if num > 3:
            break
        if r_article.headline != article.headline:

            # 第一个字符
            article_headline_chars = []
            r_article_headline = r_article.headline.replace(" ", "").replace("\n", "")
            # for c in r_article_headline:
            #     article_headline_chars.append(c)

            headline = article.headline.replace(" ", "").replace("\n", "")
            print(r_article_headline[0])
            if r_article_headline[0] in headline:
                r_articles_result.append(r_article)
                num += 1


    if len(r_articles_result) < 4:
        r_articles = Article.objects.order_by('-pageviews')[:4-len(r_articles_result)]

        r_articles_result.extend(r_articles)

    return r_articles_result
