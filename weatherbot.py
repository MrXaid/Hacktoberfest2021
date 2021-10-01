import math
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.speak(str)
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key = 'd0d916a4d978d5defe65fbeda067fa59'


def get_weather(city):
    """

    :type city: object
    """
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_Celsius = temp_kelvin - 273.15
        temp_Fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        c = str(math.trunc(temp_Celsius)) + "  degree Celsius"
        k = str(math.trunc(temp_kelvin)) + "kelvin"
        f = str(math.trunc(temp_Fahrenheit)) + "fahrenheit"
        final = [city, country, k, c, f]

        #final: typing.List[typing.Union[typing.Union[float, int], typing.Any]] = [city, country, temp_Celsius,
                                                                                  #temp_Fahrenheit, icon, weather]
        return final

    else:
        return None


cit = str(input("Enter City Name you want to weather of: "))
print(get_weather(cit))
#speak(str(get_weather(cit)))
