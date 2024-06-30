from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=2000)
    status_code = models.IntegerField(null=True)
    is_ok = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.status_code=}, {self.url=}'
