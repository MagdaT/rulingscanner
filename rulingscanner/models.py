from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

HINT_MAXIMUM_LENGTH = 300
HINT_TITLE_MAXIMUM_LENGTH = 30
TAG_MAXIMUM_LENGTH = 150
MAXIMUM_COMMENT_LENGTH=1000


class Tag( models.Model ):
    name = models.CharField( max_length=TAG_MAXIMUM_LENGTH )

    def __str__(self):
        return self.name


class Authors( models.Model ):
    name = models.CharField( max_length=400)

    def __str__(self):
        return self.name


class TaxType( models.Model ):
    name = models.CharField( max_length=150)

    def __str__(self):
        return self.name


class Ruling( models.Model ):
    content = models.CharField( max_length=500000, null=True )
    title = models.CharField( max_length=500000, null=True )
    creation_date = models.DateTimeField( auto_now_add=True )
    tags = models.ManyToManyField( Tag, blank=True, null=True, related_name="tag" )
    important_ruling = models.BooleanField( default=False )
    important_by_user = models.ManyToManyField( User, related_name="likes", blank=True )
    authority = models.ManyToManyField( Authors)
    type_of_tax = models.ManyToManyField( TaxType, default=None, related_name="tax_type")
    positive_ruling = models.BooleanField( null=False )
    ruling_no = models.CharField( max_length=150, null=True )
    mf_library_no = models.CharField( max_length=150, null=True )

    @property
    def get_shortcut(self):
        return " ".join( self.content.split()[:10] ) + "..."

    @property
    def get_shortcut_important_ruling(self):
        return " ".join( self.content.split()[:160] ) + "..."

    def __str__(self):
        return '[{}] {}: {}'.format(
            self.creation_date,
            self.title, self.content[:40] )


class Comment(models.Model):
    content = models.CharField(max_length=MAXIMUM_COMMENT_LENGTH)
    date_comment = models.DateTimeField(auto_now_add=True)
    ruling = models.ForeignKey(Ruling, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content