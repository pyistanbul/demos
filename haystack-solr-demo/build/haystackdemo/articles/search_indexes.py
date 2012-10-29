from datetime import datetime

from haystack.indexes import *
from haystack import site

from articles.models import Article


class ArticleIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr="author")
    creation_date = DateTimeField(model_attr="creation_date")


site.register(Article, ArticleIndex)
