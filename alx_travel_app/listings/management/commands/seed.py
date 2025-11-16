from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Optional: Clear old data
        Listing.objects.all().delete()

        for _ in range(10):  # Create 10 sample listings
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                price_per_night=random.randint(50, 500),
                location=fake.city(),
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings."))
