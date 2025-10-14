"""
    In this project we allow the user to introduce a city and get information about the weather of that city at the moment of
    the introduction. We alse take into consideration the edge cases and treat them so that the user's experiece is flowless. 
"""

import requests

# Function that changes the temperature to celsiul, and allows to have only 2 digits after the intenger number, using round
def change_to_celsius(temp_in_kelvin):
    return round(temp_in_kelvin-273.15,2)

# Function that takes the name of the city from the user
def get_info():
    print("Thank you for choosing out app. For getting informations about the weather introduce the name of the city:")
    city=input()
    return city

# Function that calls the OpenWeatherAPI and returns the json file if everything went great or None if there was a problem
def api_call(city_name):
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    key="1a96893db020a346f3355d7bb78a2f04"
    url=base_url+f"q={city_name}"+"&"+"lang=en"+"&"+f"appid={key}"

    response=requests.get(url)

    if response.status_code==200:
        return response.json()
    elif response.status_code==404:
        print("Something went wrong. Please try again and introduce the city that you want")
    
    return None

# Function that shows all the info that a user might need about the weather from the city chosen
def show_info(response):
    print(f"Weather: {response['weather'][0]['main']}")
    print(f"Description: {response['weather'][0]['description']}")
    print(f"Temperature: {change_to_celsius(response['main']['temp'])}")
    print(f"Feels like: {change_to_celsius(response['main']['feels_like'])}")
    print(f"Min. Temperature: {change_to_celsius(response['main']['temp_min'])}")
    print(f"Max. Temperature: {change_to_celsius(response['main']['temp_max'])}")
    print(f"Humidity: {response['main']['humidity']}%")

# The main function that calls for the others in the right order
def main():
    city=get_info()
    response_dict=api_call(city)
    if response_dict!=None:
        show_info(response_dict)

# We call the main function here
if __name__=="__main__":
    main()