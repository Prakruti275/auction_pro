from django.contrib import admin
from .models import AuctionItem, Bid, AuctionBot

@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'current_bid', 'starting_bid', 'end_time']

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'bidder', 'bid_amount', 'time']

@admin.register(AuctionBot)
class AuctionBotAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'max_auto_bid', 'active']

from django.contrib import admin

# Change the site header
admin.site.site_header = "AMNS Auction Admin"

# Change the site title (text shown on browser tab)
admin.site.site_title = "AMNS Admin Portal"

# Change the index title (dashboard heading)
admin.site.index_title = "Welcome to the AMNS Auction Dashboard"
