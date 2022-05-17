import requests
from pprint import pprint

class OpenWeather:
  def __init__(self):   
    '''
    desc: initializes the variables needed for the program to run
    arg= none
    return= none
    '''
    self.city = city
    self.temp_max = temp_max
    self.temp_min = temp_min
    self.desc= desc
    self.humid= humid 
    self.windspd= windspd
    

  def __str__():
    '''
    desc= connects the api url, also prints the weather forecast in accordance to your city
    arg= none
    return= none
    
    '''

    api_url = "http://api.openweathermap.org/data/2.5/weather"


    city = input("What city are you in? ")
    
    params = {
        'q': city,
        'appid': '255993d2f96389e39e787231ff82c662', 
        'units': 'imperial'
        }
    
    res = requests.get(api_url, params=params)
    
    data = res.json()
    pprint(data)
    
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]
    desc= data['weather'][0]['description']
    humid = data['main']['humidity']
    windspd= data['wind']['speed']

    print('')
    print('')
    print('')
    print('┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑')
    print("  Weather Forecast in "+city)
    print('└────────────────────────────┘')
    
    print("In "+city+" the high is "+str(temp_max) +"°F"+" and the low is "+ str(temp_min )+"°F.")

    print("Weather Description: "+desc)
    print("Humidity: ",humid,"%")
    print("Wind Speed: ",windspd,"mph")
        
    
    print ("") 
    print ("") 
    print ("") 
  
  
  