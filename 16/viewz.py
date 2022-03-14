from modelz import Article
from owner import (
    OwnerListView,
    OwnerDetailView,
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
)


class ArticleListView(OwnerListView):
    model = Article


class ArticleDetailView(OwnerDetailView):
    model = Article


class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ["title", "text"]


class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ["title", "text"]


class ArticleDeleteView(OwnerDeleteView):
    model = Article
