from django.shortcuts import render
from django.http import Http404 , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

# List of Challenges that we have
monthly_challenges = {
    "january" :"Eat no meat for the entire month!",
    "febraury" :"Walk for at least 30 min every day!",
    "march": "Learn Django every day at least for 20 mins",
    "april": "Learn Django every day at least for 20 mins",
    "may": "Learn Django every day at least for 20 mins",
    "june": "Learn Django every day at least for 20 mins", 
    "july": "Learn Django every day at least for 20 mins",
    "august": "Learn Django every day at least for 20 mins",
    "september" : "Learn Django every day at least for 20 mins",
    "october": "Learn Django every day at least for 20 mins",
    "december": None,
    "november":"Sleep before 12"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request , "challenges/index.html" , {
        "months": months
    })



#Converting the number to the month in the list
def monthly_challenge_by_number(request , month):
    #We extract all of the keys in monthly_challenge list and we list them by list()
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    #using a littel bit fourmula for converting arrys and list logic to the Real life and user logic
    redirect_month = months[month - 1]
    #month-challenge comes from urls.py file that we named it. args will be the argument that we put after the url that we set in urls.py
    redirect_path =reverse("month-challenge" , args = [redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request , month):
    #using try and catch method for unexpected erors
    try:
        challenge_text = monthly_challenges[month]
        return render(request , "challenges/challenge.html" , {
            "text": challenge_text,
            "month_name": month
        } )
    except:
        raise Http404()
    