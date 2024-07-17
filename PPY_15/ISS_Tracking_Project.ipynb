"""
International Space Station (ISS) Tracking Project

Project Description:
This app will email you based on the event that the International Space Station (ISS)
is above of us in the sky, at night. We make three methods to achieve this mission:

 is_night()
 is_overhead()
 send_email()

This App will e-mail you when the ISS is overhead, and it is night in your location.
No email otherwise :/

We test this in our location (Brazil). @see Resources
(please enter your lat and lng data to personalize the app for your need).

    MY_LAT = <your_lat>
    MY_LNG = <your_lng>

Now some curiosities about ISS:

Can you see the International Space Station in the night sky?
Image result for the event that the international station are above of us in the sky, at night.
Did you know that you can see the International Space Station ( ISS ) in the night sky as it passes
 over your area at a distance of approximately 400 km from Earth? To the naked eye, the Space Station
 looks like a big white dot that moves quickly across the sky without changing direction, unlike aircraft,
 for example.

Can I track the ISS from my location?
Image result for this code will track the iss in the sky, comparing to your location and time.
The space station can be seen from over 6,700 locations worldwide. Enter your location to find out
when the space station will be flying overhead.

Is the ISS visible every night?
It can only be seen when it is dawn or dusk at your location.
As such, it can range from one sighting opportunity a month to several a week,
since it has to be both dark where you are, and the space station has to happen to be going overhead.

Possible error: (Report API abuse - Max retries exceeded)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api.sunrise-sunset.org', port=443): Max retries exceeded
with url: /json?lat=-8.76107&lng=-63.88598&formatted=0&date=today
(Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f52ad76bd60>:
Failed to establish a new connection: [Err no -3] Temporary failure in name resolution'))

Resources:

JSON Viewer - Chrome Web Store:
https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh

Latitude and Longitude Finder:
https://www.latlong.net/

Sunset and sunrise times API:
https://sunrise-sunset.org/api

International Space Station Current Location:
http://open-notify.org/Open-Notify-API/ISS-Location-Now/
Location: Porto Velho Ro - Brazil

Output:
#####################################
Local time: 5 hours
Is not night :/

iss_lat:23.6524, iss_lng:-41.0131
my__lat:-8.76107,my__lng:-63.88598
ISS is not overhead :/

Process finished with exit code 0
####################################

How-to run (PyCharm 2022.3 (Community Edition):
0) Open Pycharm, Clone this project by clicking Clone > VCS
   now, Git > Manage remotes... click + and paste:
   url: https://github.com/giljr/iss_tracking.git
1) Run -> Edit Configurations -> Set Project Interpreter (lasted version - mine is Python 3.10)
2) pip install requests (Terminal)
3) pip install yagmail (Terminal)
4) Go To Edit Configuration...Environment > Env. Variables
   and add two variable:

   EMAIL=<your_email>@gmail.com;
   EMAIL_PASS=<app_password>

   Sign in with App Passwords by following this tutorial:
   (https://support.google.com/accounts/answer/185833)
5) run main (Shift+F10)

Making ISS project, I was inspired by Angela Yu , App Brewery.
https://www.udemy.com/course/100-days-of-code/

@editor: j3
Date: Dez, 2022
"""

from datetime import datetime, timedelta
import requests
import yagmail
import os


MY_LAT = -8.761070
MY_LNG = -63.885980

timezone_hour_offset = -4
input_format = "%Y-%m-%dT%H:%M:%S+00:00"  # works for this site because UTC is guaranteed.
output_format = "%H:%M:%S"

EMAIL = os.environ['EMAIL']
EMAIL_PASS = os.environ['EMAIL_PASS']

'''
The ISS is visible only at night :/
'''


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "date": "today",
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_date_time = data["results"]["sunrise"]
    sunset_date_time = data["results"]["sunset"]

    sunrise = datetime.strptime(sunrise_date_time, input_format)
    local_sunrise = sunrise + timedelta(hours=timezone_hour_offset)

    sunset = datetime.strptime(sunset_date_time, input_format)
    local_sunset = sunset + timedelta(hours=timezone_hour_offset)
    local_sunrise_hour = local_sunrise.hour
    local_sunset_hour = local_sunset.hour
    time_now = datetime.now().hour
    print(f"Local time: {time_now} hours")
    if time_now >= local_sunset_hour or time_now <= local_sunrise_hour:
        return True


'''
Spot the Station" find out if the International Space Station, 
the third brightest object in the sky, is going to pass above your location.
Your position is within + or - 5 degrees of the ISS position.
'''


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    print(f"iss_lat:{iss_lat}, iss_lng:{iss_lng}")
    print(f"my__lat:{MY_LAT},my__lng:{MY_LNG}")
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= iss_lng + 5:
        return True


'''
Sends alerts via your email using yagmail.
Please set environment variables in PyCharm, follow stackoverflow:
https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm
'''


def send_email():
    user = yagmail.SMTP(user=EMAIL, password=EMAIL_PASS)
    user.send(to=EMAIL, subject="Look Up 👆️", contents="The ISS is above you in the sky.")


is_dark = is_night()
if is_dark is True:
    print("Is night :)")
else:
    print("Is not night :/\n")

is_over = is_iss_overhead()
if is_over is True:
    print("ISS is overhead :)")
else:
    print("ISS is not overhead :/ ")

if is_over is True and is_dark is True:
    send_email()
