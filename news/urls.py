from django.urls import include, path
from . import views
from django.conf.urls import url

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
]
