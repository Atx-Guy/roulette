import random
import os
from django.shortcuts import redirect, render
from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.core.wsgi import get_wsgi_application

# Ensure settings are only configured once
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
        INSTALLED_APPS=["django.contrib.staticfiles"],
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": ["templates"],
                "APP_DIRS": True,
            }
        ],
        STATIC_URL="/static/",
    )

application = get_wsgi_application()

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

def random_website(request):
    url = random.choice(WEBSITES)
    return redirect(url)

def home(request):
    return render(request, "roulette/index.html")

# Django URL Configuration
urlpatterns = [
    path("", home, name="home"),
    path("random", random_website, name="random_website"),
]

# Template (HTML) file content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rushin' Roulette</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="d-flex justify-content-center align-items-center vh-100 bg-light">
    <div class="text-center">
        <h1 class="mb-4">Rushin' Roulette</h1>
        <p class="mb-3">Press the button to visit a random website!</p>
        <a href="/random" class="btn btn-danger btn-lg">Rushin' Roulette</a>
    </div>
    <script>
        document.querySelector(".btn-danger").addEventListener("click", function() {
            window.location.href = "/random";
        });
    </script>
</body>
</html>
"""

# Ensure templates directory exists
os.makedirs("templates/roulette", exist_ok=True)

# Save the HTML content
with open("templates/roulette/index.html", "w") as f:
    f.write(html_content)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    import sys

    execute_from_command_line(sys.argv)
