from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from faker.providers import internet, misc
import random
from django.db.models.aggregates import Count
from random import randint

from rulingscanner import models

NO_OF_NEW_RULINGS = 10
RULING_MAX_LENGTH = 1500


#
# content = models.CharField( max_length=500000, null=True )
#     title = models.CharField( max_length=500000, null=True )
#     creation_date = models.DateTimeField( auto_now_add=True )
#     tags = models.ManyToManyField( Tag, blank=True, null=True, related_name="tag" )
#     important_ruling = models.BooleanField( default=False )
#     important_by_user = models.ManyToManyField( User, related_name="likes", blank=True )
#     authority = models.ManyToManyField( Authors)
#     type_of_tax = models.ManyToManyField( TaxType, default=None, related_name="tax_type")
#     positive_ruling = models.BooleanField( null=False )
#     ruling_no = models.CharField( max_length=150, null=True )
#     mf_library_no = models.CharField( max_length=150, null=True )


# UWAGA! niedokończone - nie wszystkie pola w modelu generują się

class Command(BaseCommand):
    help = 'Generates random rulings'

    def handle(self, *args, **options):
        fake = Faker('pl_PL')
        fake.add_provider(internet)
        fake.add_provider(misc)

        for _ in range(NO_OF_NEW_RULINGS):

                ruling = models.Ruling( title=fake.text( max_nb_chars=
                                         models.HINT_TITLE_MAXIMUM_LENGTH ),
                                      content=fake.text(
                                         max_nb_chars=
                                         models.HINT_MAXIMUM_LENGTH),
                                      )
                ruling.save()
