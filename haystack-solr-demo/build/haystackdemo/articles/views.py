from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from articles.models import Article


def detail(request, slug):
    """
    Renders the detail page for an Article
    """
    article = get_object_or_404(Article.objects, slug=slug)

    return render_to_response("articles/detail.html", {
        "article": article,
    }, context_instance=RequestContext(request))
