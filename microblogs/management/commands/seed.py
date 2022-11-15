from django.core.management.base import BaseCommand, CommandError
from faker import Faker


class Command(BaseCommand):

    def __init__():
        super().__init__()
        self.faker = Faker('en_GB')


    def handle(self, *args, **options):
        print("Warning: the seed command has not been implemented yet")