from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    """Custom class used for creating development data in database tables """
    
    help = 'Loads the initial data about insurance app into a database'

    def handle(self, *args, **options):
        call_command('loaddata', 'field_type.json', verbosity=0)
        call_command('loaddata', 'field.json', verbosity=0)
        call_command('loaddata', 'risk_type.json', verbosity=0)
        return "Initial data created successfully"