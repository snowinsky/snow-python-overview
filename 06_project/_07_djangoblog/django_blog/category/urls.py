from django.urls import path
from category.views import DashboardView, ArticleView, ArticleDeleteView

app_name = "category"

urlpatterns = [

    path("dashboard/",    DashboardView.as_view(),    name="dashboard"),
    path("article/",    ArticleView.as_view(),    name="article"),
    path("article_del/",    ArticleDeleteView.as_view(),    name="article_del"),
]