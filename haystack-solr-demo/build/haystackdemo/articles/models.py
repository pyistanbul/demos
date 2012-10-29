from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    """
    An article with a specific time stamp and author
    """
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    author = models.ForeignKey("auth.User", verbose_name=_("Author"), related_name="articles")
    body = models.TextField(_("Body"), blank=True)
    creation_date = models.DateTimeField(_("Creation Date"), default=datetime.now)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ["creation_date"]

    def __unicode__(self):
        return u"%(title)s by %(author)s" % {
            "title": self.title,
            "author": self.author,
        }

    @models.permalink
    def get_absolute_url(self):
        return ("articles_detail", (), {
            "slug": self.slug,
        })
