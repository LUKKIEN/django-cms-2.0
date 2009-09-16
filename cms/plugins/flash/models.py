import re
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.models import CMSPlugin
from os.path import basename

from filebrowser.fields import FileBrowseField

class Flash(CMSPlugin):
    file = FileBrowseField( max_length        =512,
                            initial_directory ='/',
                            extensions_allowed=['.swf'] )
    width = models.CharField(_('width'), max_length=6)
    height = models.CharField(_('height'), max_length=6)    
    
    def get_height(self):
        return fix_unit(self.height)
    
    def get_width(self):
        return fix_unit(self.width)    
        
    def __unicode__(self):
        return u"%s" % basename(self.file.original)

def fix_unit(value):
    if not re.match(r'.*[0-9]$', value):
        # no unit, add px
        return value + "px"
    return value 
