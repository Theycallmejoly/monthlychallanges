from django.urls import path
from . import views

urlpatterns = [
#Using empty string to acces the main page that means Challenges page
path("" , views.index , name="index"),
path("<int:month>" , views.monthly_challenge_by_number ),
#Setting the name for using the reverse utility function. Read more in views.py file.
path("<str:month>" , views.monthly_challenge , name="month-challenge")
]