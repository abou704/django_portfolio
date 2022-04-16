from django.db import models
from django.core.exceptions import ObjectDoesNotExist


import logging

logger = logging.getLogger(__name__)


TOLERANCE_FLOAT_EQUAL = 1e-10

class OfsModelManager(models.Manager):

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None
    
    def get_or_none_with_related(self, sel_related, **kwargs):
        try:
            return self.select_related(*sel_related).get(**kwargs)
        except ObjectDoesNotExist:
            return None



class OfsModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def _for_same(self):
        return []

    def same(self, ctr):
        left = self._for_same()
        right = ctr._for_same()
        are_same =  (left == right) and len(right) > 0
        return  are_same

    class Meta:
        abstract = True