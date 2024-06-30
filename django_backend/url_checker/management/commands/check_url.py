from django.core.management.base import BaseCommand

from url_checker.models import Url
from ._base import check


class Command(BaseCommand):
    help = 'HTTP GET request url, write response status code to database'

    def handle(self, *args, **options) -> str | None:
        url = options.get('url')
        status_code = check(url=url)
        is_ok = False
        if status_code:
            is_ok = status_code//100 == 2
        print(status_code)
        try:
            url_object = Url.objects.get(url=url)
            url_object.status_code, url_object.is_ok = status_code, is_ok
            url_object.save()
        except Url.DoesNotExist:
            Url.objects.create(url=url, status_code=status_code, is_ok=is_ok)
    
    def add_arguments(self, parser):
        parser.add_argument('-u', '--url', help='URL to check')
