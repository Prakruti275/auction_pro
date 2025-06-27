from django.shortcuts import render, get_object_or_404, redirect
from .models import AuctionItem, Bid
from .forms import BidForm
from .bot import trigger_bot  # if your bot logic is in a separate file

def place_bid(request, item_id):
    item = get_object_or_404(AuctionItem, id=item_id)
    form = BidForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        bid_amount = form.cleaned_data['bid_amount']
        if bid_amount > item.current_bid:
            Bid.objects.create(item=item, bidder=request.user, bid_amount=bid_amount)
            item.current_bid = bid_amount
            item.save()
            trigger_bot(item)
            return redirect('place_bid', item_id=item.id)  # refresh the page

    return render(request, 'auction/item.html', {'item': item, 'form': form})

def index(request):
    items = AuctionItem.objects.all()
    return render(request, 'auction/index.html', {'items': items})
