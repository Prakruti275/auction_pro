from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('item/<int:item_id>/bid/', views.place_bid, name='place_bid'),

]


