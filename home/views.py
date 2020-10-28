from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import City
from .forms import CityForm
import requests


def index(request):
    form = CityForm()
    if request.method=="POST":

        form = CityForm(request.POST)
    
        form.save()
    

    cities = City.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=matric&appid={YOUR API KEY}'

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city.name)).json()

        weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'humidity' :  str(r['main']['humidity']) + " %",
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)
  
    return render(request,'weather.html', {'weather_data':weather_data})


def delete(request, city):
	city = City.objects.filter(name=city).order_by('id').first()
	city.delete()
	return redirect("/")