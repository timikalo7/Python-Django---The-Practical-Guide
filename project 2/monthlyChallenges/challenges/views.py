from django.shortcuts import render
# importing httpresponse so we can print on page etc
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect , Http404
from django.urls import reverse

# making a folder called challenges to be more efficient
challenges = {
    "january": "jan",
    "february": "feb",
    "march": "mar",
    "april": "apr",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "aug",
    "september": "sep",
    "october": "oct",
    "november": "nov",
    "december": "dec"
}
# function to go to main challenges page


def index(request):
    months = list(challenges.keys())
    return render(None,"challenges/index.html", {
        "months":months
    } )

# function that checks the month
def monthlyChallengesByNumber(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month buddy")

    redirectMonth = months[month - 1]

    # /challenge/january
    redirectPath = reverse("month-challenge", args=[redirectMonth])
    return HttpResponseRedirect(redirectPath)

# func that checks the month and what u should print if it comes and if they r silly says 404


def monthlyChallenges(request, month):
    try:
        challenge_text = challenges[month]
        responseData = render(None, "challenges/challenge.html",{
                            "text": challenge_text
                            })
        return HttpResponse(responseData)
    except:
        raise Http404()