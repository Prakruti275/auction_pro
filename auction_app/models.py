# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class AuctionItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.FloatField()
    current_bid = models.FloatField(default=0)
    max_bid_limit = models.FloatField(default=10000)
    end_time = models.DateTimeField()

class Bid(models.Model):
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

class AuctionBot(models.Model):
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    max_auto_bid = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Bot for {self.item.title} (Max ₹{self.max_auto_bid})"
