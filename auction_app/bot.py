import threading
import time
from .models import AuctionBot, Bid

def trigger_bot(item):
    bots = AuctionBot.objects.filter(item=item, active=True)

    for bot in bots:
        if item.current_bid + 10 <= bot.max_auto_bid:
            def auto_bid():
                time.sleep(0.5)  # simulate bot thinking
                item.refresh_from_db()

                # Check again to avoid race condition
                if item.current_bid + 10 <= bot.max_auto_bid:
                    new_bid = item.current_bid + 10
                    item.current_bid = new_bid
                    item.save()
                    Bid.objects.create(
                        item=item,
                        bidder=None,  # No human user; it's a bot
                        bid_amount=new_bid
                    )

            # Run bot in background thread
            threading.Thread(target=auto_bid).start()
