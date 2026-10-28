
from django.shortcuts import render

def home(request):
    films = [
        {"name": "Joker", "IMBD": 7.5},
        {"name": "Inception", "IMBD": 8.8},
        {"name": "Interstellar", "IMBD": 8.7},
        {"name": "Titanic", "IMBD": 7.9},
        {"name": "The Dark Knight", "IMBD": 9.0},
    ]

    return render(request, "films.html", {"films": films})
