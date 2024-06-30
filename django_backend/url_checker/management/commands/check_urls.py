from datetime import datetime, timezone, timedelta

from django.core.management.base import BaseCommand

from ._base import check
from url_checker.models import Url


class Command(BaseCommand):
    help = 'HTTP GET request urls, write response status codes to database'

    def handle(self, *args, **options) -> str | None:
        start_datetime = datetime.now(timezone.utc)
        end_datetime = start_datetime - timedelta(minutes=5)
        url_objects = Url.objects.filter(modified_date__lte=end_datetime)
        for url_object in url_objects:
            status_code = check(url=url_object.url)
            is_ok = status_code//100 == 2
            print(f'{url_object.id=}, {url_object.url=}, {status_code=}')
            url_object.status_code, url_object.is_ok = status_code, is_ok
            url_object.save()
            if start_datetime + timedelta(minutes=5) > datetime.now(timezone.utc):
                break
