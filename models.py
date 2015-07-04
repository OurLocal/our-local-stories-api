from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.postgres.fields import ArrayField
from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField


class Story(models.Model):
    title = models.TextField()
    url = models.URLField()
    date = models.DateField()
    primary_image = models.URLField(null=True)
    primary_image_caption = models.TextField(null=True)
    primary_image_rights_information = models.TextField(null=True)
    subjects = models.TextField(null=True)
    station = models.TextField(null=True)
    state = models.TextField(null=True)
    place = models.TextField(null=True)
    keywords = models.TextField(null=True)
    location = PointField()

    search_index = VectorField()

    objects = SearchManager(
        fields = ('title', 'primary_image_caption'),
        config = 'pg_catalog.english',
        search_field = 'search_index',
        auto_update_search_field = True
    )
