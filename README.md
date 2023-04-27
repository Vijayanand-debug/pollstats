=====
pollstats
=====

Pollstats is a Django app which display the entire number of Voters, calculates the percentage of voters who took part in the 
online poll. This library is exclusively designed for a college project and may not have all the dynamic features.

Quick start
-----------

1. Add "pollstats.apps.PollstatsConfig" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'pollstats.apps.PollstatsConfig',
    ]

2. Include the polls URLconf in your project urls.py like this::
    path('pollstats/',include("pollstats.urls")),

3. This library uses Django's default User Object and the data in it is accessed by using from django.contrib.auth.models import User

4. This library strictly uses the following models to calculate the data:
    
    class Events(models.Model):
     event_name = models.CharField(max_length=200)
     event_code = models.CharField(max_length=20)
     referal_code = models.CharField(max_length=20)
     hosted_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
     event_description = models.TextField()
     event_status = models.IntegerField(default=0)
     starting_date = models.DateField(default=None)
     ending_date = models.DateField(default=None)

    class Options(models.Model):
     option_name = models.CharField(max_length=100)
     count = models.IntegerField(default=0)
     event_code = models.CharField(max_length=200)
    
    class Transactions(models.Model):
     voter = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
     voting_time = models.DateTimeField(auto_now_add=True) 
     option_name = models.CharField(max_length=150)
     event_name = models.CharField(max_length=150)  
     event_code = models.CharField(max_length=70)
     referal_code = models.CharField(max_length=70)

5. Django admin can be used to insert the data in to Events table and also to insert initial data in to Options table with 
   count as 0

6. Then the count should be updated when a user votes/unvotes, the data in Transactions table must be inserted and deleted
   during the vote/unvote process

   