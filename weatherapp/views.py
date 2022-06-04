from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=PUTYOURAPIID').read()
        json_data=json.loads(res)
        data={
            'country_code':str(json_data['sys']['country']),
            'temp':str(json_data['main']['temp']),
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity']),
            'rain':str(json_data['weather'][0]['main']),
            'description':str(json_data['weather'][0]['description']),
            'icon':json_data['weather'][0]['icon'],
            'name':str(json_data['name']),
        }

    else:
        data={}
    return render(request,'index.html',data)
