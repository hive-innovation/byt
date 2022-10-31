from email.policy import default
from django.db import models
import datetime
# database for search- queries
class search_query(models.Model):
    search_query = models.TextField(blank=False)
    date_of_query = models.DateTimeField(default=datetime.datetime.utcnow)
    def __str__(self):
        return self.search_query
