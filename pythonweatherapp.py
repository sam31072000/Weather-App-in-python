import requests , time , threading
from win10toast import ToastNotifier
ipinfo = requests.get("https://ipapi.co/json").json()   #ipapi is used to get the current ip address with location
city = ipinfo['city']
weatherapi = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6b70db340cd49ddb47c6d2e7445222f5"
def showweather():
    weather = requests.get(weatherapi).json()
    condition = weather["weather"][0]["description"]
    temp = weather["main"]["temp"] - 273.15
    notif = ToastNotifier()
    notif.show_toast(f"The Current Weather of {city} is",f"Its's {condition}, currently temperature is {temp} centigrade")  #show notifications
    threading.Timer(1000*3600,showweather).start()   #show after 1 hr and to stop ctr+c
showweather()
