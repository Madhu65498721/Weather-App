from django.shortcuts import render, HttpResponse
import json
import requests
from django.conf import settings

# Create your views here.
def weather(request):
    data = {}  # Initialize data as an empty dictionary
    if request.method == 'POST':
        city = request.POST.get('city', '')
        source = f"http://api.openweathermap.org/data/2.5/weather?q={{}}&units=imperial&appid={settings.OPENWEATHER_API_KEY}"
        response = requests.get(source.format(city))
        list_of_data = response.json()

        if response.status_code == 200:
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "city": str(list_of_data['name']),
                "longitude": str(list_of_data['coord']['lon']),
                "latitude": str(list_of_data['coord']['lat']),
                "temp": round((list_of_data['main']['temp'] - 32) * 5.0 / 9.0, 2),
                "temperature_fahrenheit": list_of_data['main']['temp'],
                "humidity": str(list_of_data['main']['humidity']),
                "description": str(list_of_data['weather'][0]['description']),
                "speed": str(list_of_data['wind']['speed']),
            }
        else:
            data['error'] = "Oops! That city doesn’t seem to exist. Double-check the spelling."
    return render(request, "weather.html", data)
