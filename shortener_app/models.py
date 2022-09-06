from django.db.models import Model, CharField, URLField
from shortener_app.utils import alias_generator

# Create your models here.


class AliasedUrl(Model):
    alias = CharField(max_length=8, default=alias_generator, primary_key=True)
    url = URLField(blank=False)

    def __str__(self):
        return f"{self.alias} -> {self.url}"
