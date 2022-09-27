from django.db import models

# database for search- queries
class search_query(models.Model):
    search_query = models.TextField(blank=False)
    date_of_query = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.search_query
