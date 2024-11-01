from django.db import models

class Genre(models.Model):
  id = models.CharField(max_length=50, primary_key=True)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.description

class PriceOverview(models.Model):
  currency = models.CharField(max_length=10)
  initial = models.IntegerField()
  final = models.IntegerField()
  discount_percent = models.IntegerField()
  initial_formatted = models.CharField(max_length=50, blank=True)
  final_formatted = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.currency} {self.final_formatted}"

class Wishlist(models.Model):
  name = models.CharField(max_length=400)
  steam_appid = models.CharField(max_length=20)
  price_overview = models.OneToOneField(PriceOverview, on_delete=models.CASCADE)
  description = models.TextField()
  genres = models.ManyToManyField(Genre)
  header_image = models.URLField()

  def __str__(self):
    return self.name
