from django.core.management.base import BaseCommand

from Scraping_srver.zvk.models import Zvk


class Command(BaseCommand):
    help = 'Fill database with zvk'

