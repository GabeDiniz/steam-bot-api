from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Wishlist
    fields = ("id", "name", "steam_appid", "price_overview", "description", "genres", "header_image")