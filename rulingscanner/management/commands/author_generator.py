# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from faker import Faker
# from faker.providers import internet, misc
#
# from rulingscanner import models
#
# NO_OF_NEW_TAGS = 10
#
#
# class Command(BaseCommand):
#     help = 'Generates random tags'
#
#     def handle(self, *args, **options):
#         fake = Faker('pl_PL')
#         fake.add_provider(internet)
#         fake.add_provider(misc)
#
#         for _ in range(NO_OF_NEW_TAGS):
#
#                 tag = models.Tag(
#                                    name = fake.text(max_nb_chars=models.TAG_MAXIMUM_LENGTH))
#                 tag.save()
