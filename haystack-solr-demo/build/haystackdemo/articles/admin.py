from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "creation_date")
    search_fields = ("body", "title", "author__first_name", "author__last_name")

    save_on_top = True
    
    prepopulated_fields = {
        "slug" : ("title",),
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug"), "author", "body", "creation_date"),
        }),
    )

admin.site.register(Article, ArticleAdmin)
