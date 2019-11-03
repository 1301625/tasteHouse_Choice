from django.db import models

# Create your models here.
class Houses(models.Model):
    store_title = models.CharField(max_length=100)
    store_category = models.CharField(max_length=50)
    store_review = models.CharField(max_length=150, null=True)
    store_price = models.CharField(max_length=50, null=True)
    store_address = models.CharField(max_length=200 , null=True)
    store_tags = models.CharField(max_length=100 , null=True)

    store_img = models.URLField(null=True)


    def __str__(self):
        return self.store_title