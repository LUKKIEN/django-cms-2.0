from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

from cms.utils.helpers import reversion_register

# Stores the actual data
class Snippet(models.Model):
    """
    A snippet of HTML or a Django template
    """
    name = models.CharField(_("name"), max_length=255, unique=True)
    html = models.TextField(_("HTML"), blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

# Plugin model - just a pointer to Snippet
class SnippetPtr(CMSPlugin):
    snippet = models.ForeignKey(Snippet)

    class Meta:
        verbose_name = _("Snippet")
        
    search_fields = ('snippet__html',)

    def __unicode__(self):
        # Return the referenced snippet's name rather than the default (ID #)
        return self.snippet.name


    def __unicode__(self):
        return self.snippet.name

reversion_register(Snippet)

