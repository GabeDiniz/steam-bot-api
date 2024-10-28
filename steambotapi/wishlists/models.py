from django.db import models

class Wishlist(models.Model):
  name = models.CharField(max_length=400)
  language = models.CharField(max_length=400)
  price = models.CharField(max_length=20)

  def __str__(self):
    return self.name