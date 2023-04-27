from django.urls import path
from . import views

urlpatterns = [
    path('getusernumbers/<event_code>', views.getusernumbers),
]