from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, auth
from voting_app.models import Transactions

# Create your views here.
def getusernumbers(event_code,event_id):

    stats= {}
    count= 0
    transaction_count=0
    vote_percentage= 0

    user_details= User.objects.filter()
    if user_details.exists:
     for u in user_details:
        count= count + 1

    transactions= Transactions.objects.filter(event_code=event_code)
    if transactions.exists:
     for t in transactions:
        transaction_count=transaction_count + 1

    if count > 0:
      vote_percentage= round((transaction_count / count) * 100, 2)
      stats['entire_user_count'] = count
      stats['voted_count'] = transaction_count
      stats['vote_percent'] = vote_percentage
      stats['event_id'] = event_id

    return stats