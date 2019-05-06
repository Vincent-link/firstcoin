from django.urls import include, path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
]
