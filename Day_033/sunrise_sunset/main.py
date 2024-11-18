import requests
from datetime import datetime
import pytz
import smtplib
import os

def clear_console():
    '''This is only for console on windows to remove the password from the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

email = input("Enter your Email that will send this info.: ")
password = input("\nEnter your app password "
                           "\nnote: this is for gmail only :")
send_to_email = input("\nwho do you want to send this too?: ")
clear_console()
print(f"Email is sending from: {email}\nEmail sending too: {send_to_email}\n")

my_lat = "31.50612282450553"
my_lng = "-82.85013741481139"

parameter = {
    "lat":my_lat,
    "lng":my_lng,
}

def check_for_iss():
    import requests

    api_request = requests.get(url="http://api.open-notify.org/iss-now.json")

    try:
        api_request.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError,
            requests.exceptions.Timeout, requests.exceptions.InvalidURL) as error:
        print(f"Error code {error}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        iss_data = api_request.json()
        longitude = iss_data["iss_position"]["longitude"]
        latitude = iss_data["iss_position"]["latitude"]
        return check_distance(iss_lat=latitude,iss_lng=longitude)

def check_distance(iss_lat,iss_lng):
    global my_lat,my_lng
    from geopy.distance import geodesic

    distance_to_other_point = geodesic((float(my_lat), float(my_lng)), (float(iss_lat), float(iss_lng))).km
    get_miles = round(eval(f"{distance_to_other_point} / 1.60934"), 2)

    return float(get_miles)

def convert_time(time_str,time_zone):
    ''' Place the time in and get it converted to your time zone '''
    tz = time_zone.title()
    try:
        utc_time = datetime.strptime(time_str, "%I:%M:%S %p")
        utc_time = utc_time.replace(tzinfo=pytz.UTC)
        my_tz = pytz.timezone(f"{tz}")
        return_tz = utc_time.astimezone(my_tz)
        return return_tz.strftime("%H:%M:%S")
    except ValueError:
        utc_time = datetime.strptime(time_str, "%H:%M:%S")
        utc_time = utc_time.replace(tzinfo=pytz.UTC)
        my_tz = pytz.timezone(f'{tz}')
        return_tz = utc_time.astimezone(my_tz)
        return return_tz.strftime("%H:%M:%S")

def run(users_tz):
    try:
        sunset_sunrise_api = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError,
            requests.exceptions.Timeout, requests.exceptions.InvalidURL) as error:
        print(f"Error code {error}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        api_dict = sunset_sunrise_api.json()
        for key, value in api_dict.items():
            if isinstance(value, dict):
                for key_,value_ in value.items():
                    if key_ == "sunset":
                        hr_time = convert_time(value_, users_tz).split(":")[0]
                        miles_away = check_for_iss()
                        check_view_radius(miles_away,int(hr_time))
                        # print(f"{key_}\n{hr_time}\n")
                else:
                    pass
def check_view_radius(distance,time):
    current_hour = datetime.now().hour
    print(f"ISS is {distance} Miles away. \nSunset is around : {time}:00")
    if 100 < distance < 500 and current_hour > time:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email,password)
            connection.sendmail(
                from_addr=email,
                to_addrs=send_to_email,
                msg="Subject:Look up!\n\nThe ISS is above you tonight!! its within 100-500 mile radius!")

reattempt_time = 0
mins = 60
one_hour = mins * 60

while True:
    user_input = input("\ntype in your timezone.\nExample \nUS/Eastern, US/Central, "
                                            "\nEurope/London, Europe/Paris, \nor\nUTC, GMT , CST, EST, PST: " ).title()

    hr_or_mins = input("\nType hr or mins\nTo pick your sleep time: ").lower()

    if hr_or_mins == "hr":
        while True:
            try:
                run_time = input("\nHow many hours do you want the \nprogram to sleep per try?: ")
                reattempt_time = int(run_time) * one_hour
            except Exception as error:
                print(f"whole numbers only: {error}")
            else:
                break
        break
    elif hr_or_mins == "mins":
        while True:
            try:
                run_time = input("\nHow many minutes do you want the \nprogram to sleep per try?: ")
                reattempt_time = int(run_time) * mins
            except Exception as error:
                print(f"whole numbers only: {error}")
            else:
                break
        break
    else:
        yes_or_no = input("\nSorry you something went wrong.\nTry again? yes or no?: ").lower
        if yes_or_no == "yes":
            pass
        else:
            quit()

from time import sleep
from datetime import datetime
at_t_hr = datetime.now().hour
at_t_min = datetime.now().minute

time_convert = reattempt_time
time_hours = time_convert // 3600
time_mins = (time_convert % 3600) // 60

at_t_hr += time_hours
at_t_min += time_mins

# Check if minutes exceed 60
if at_t_min >= 60:
    at_t_hr += at_t_min // 60
    at_t_min %= 60

# Check if hours exceed 24
if at_t_hr >= 24:
    at_t_hr %= 24

print(f"\n{time_hours}hours, {time_mins}minutes\n")
if len(user_input) > 0:
    while True:
        run(users_tz=user_input)
        print(f"\nSleeping till the next check.\nnext check at {at_t_hr}:{at_t_min} Zzz... Zzz...\n")
        sleep(reattempt_time)
else:
    exit()

