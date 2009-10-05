
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from os.path import basename

from django.conf import settings

from filebrowser.fields import FileBrowseField

from easymode.i18n.decorators import L10n_CMS

@L10n_CMS('alt', 'longdesc')
class Picture(CMSPlugin):
    """
    A Picture with or without a link
    """
    LEFT = "left"
    RIGHT = "right"
    FLOAT_CHOICES = ((LEFT, _("left")),
                     (RIGHT, _("right")),
                     )

    image = FileBrowseField( max_length        =512,
                             initial_directory ='/' )
    url = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True, blank=True, help_text=_("if present image will be clickable"))
    alt = models.CharField(_("alternate text"), max_length=255, blank=True, null=True, help_text=_("textual description of the image"))
    longdesc = models.CharField(_("long description"), max_length=255, blank=True, null=True, help_text=_("additional description of the image"))
    float = models.CharField(_("side"), max_length=10, blank=True, null=True, choices=FLOAT_CHOICES)
    
    def __unicode__(self):
        if self.alt:
            return self.alt[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasnt defined
            return u"%s" % basename(self.image.original)
        return "<empty>"
