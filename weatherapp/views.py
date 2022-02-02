from django.shortcuts import render
import requests
from decouple import config
# Create your views here.

def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    city = "Berlin"
    response = requests.get(url.format(city, config("API_KEY")))
    content = response.json()
    print(content)
    print(type(content))
    return render(request, "weatherapp/index.html")

