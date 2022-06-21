# importing path
from django.urls import path

# importing the views files that u made in the challenges app so u can use stuff from them
from . import views

# creating url patterns so when the months is selected makes the view run
urlpatterns = [
    path("", views.index, name = "index" ),  # will trigger if there is nothing after challenges (challenges/)
    path("<int:month>", views.monthlyChallengesByNumber),
    path("<str:month>", views.monthlyChallenges, name="month-challenge")
]
