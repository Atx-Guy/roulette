import random
from django.shortcuts import redirect, render

# List of websites to redirect to
WEBSITES = [
    "https://www.wikipedia.org/",
    "https://www.reddit.com/",
    "https://www.bbc.com/",
    "https://www.cnn.com/",
    "https://www.nationalgeographic.com/",
    "https://www.producthunt.com/",
    "https://www.stackoverflow.com/",
    "https://news.ycombinator.com/",
]

# Home View
def home(request):
    return render(request, "home.html")

# Random Website Redirect View
def random_website(request):
    url = random.choice(WEBSITES)
    return redirect(url)
