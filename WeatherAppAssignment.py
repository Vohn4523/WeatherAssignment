import geopy
from geopy.geocoders import Nominatim
import requests
API_KEY = ''
print('***********Weather App**********')
#This function will get the user to input what units of measurement they want for temp
def units_of_measurement(answer):
    # if user enter imperial or i this condition will make a api call for imperial
    if answer == 'imperial' or answer == 'i':
        user_input = input('Enter a city and state ').lower()
        weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&zip={zip}&appid={API_KEY}')
        if weather_data.json()['cod'] == '404':
            print('No City found! Please enter full city and state name or zipcode: ')
        else:
            #variables created from data that's pulled from api
            temp = round(weather_data.json()['main']['temp'])
            feels_like = round(weather_data.json()['main']['feels_like'])
            high = round(weather_data.json()['main']['temp_max'])
            low = round(weather_data.json()['main']['temp_min'])
            pressure = weather_data.json()['main']['pressure']
            description = weather_data.json()['weather'][0]['description']
            wind_speed = weather_data.json()['wind']['speed']
            geolocator = Nominatim(user_agent='WeatherProgram')
            lat = weather_data.json()['coord']['lat']
            lon = weather_data.json()['coord']['lon']
            location = geolocator.reverse(f'{lat},{lon}', language='en')
            location = location.raw['address']
            city = location['city']
            state = location['state']
            postcode = location['postcode']
            country = location['country']
            print(f'Farenheit: {temp} °F')
            print(f'feels like: {feels_like} °F')
            print(f'High: {high} °F')
            print(f'Low: {low} °F')
            print(f'Description: {description}')
            print(f'Wind: {wind_speed} km/h')
            print(f'Pressure: {pressure} hPa')
            print(f'{city}, {state}, {postcode}, {country}')

    # if user enter metric or m this condition will make a api call for metric
    elif answer == 'metric' or answer == 'm':
        if answer == 'metric' or answer == 'm':
            user_input = input('Please enter a city name, state ').lower()
            weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&zip={zip}&appid={API_KEY}')
            if weather_data.json()['cod'] == '404':
                print('No City found! Please enter full city and state name or zipcode: ')
            else:
                # variables created from data that's pulled from api
                temp = round(weather_data.json()['main']['temp'])
                feels_like = round(weather_data.json()['main']['feels_like'])
                high = round(weather_data.json()['main']['temp_max'])
                low = round(weather_data.json()['main']['temp_min'])
                pressure = weather_data.json()['main']['pressure']
                description = weather_data.json()['weather'][0]['description']
                wind_speed = weather_data.json()['wind']['speed']
                geolocator = Nominatim(user_agent='WeatherProgram')
                lat = weather_data.json()['coord']['lat']
                lon = weather_data.json()['coord']['lon']
                location = geolocator.reverse(f'{lat},{lon}', language='en')
                location = location.raw['address']
                city = location['city']
                state = location['state']
                postcode = location['postcode']
                country = location['country']
                print(f'Celsius: {temp} °C')
                print(f'feels like: {feels_like} °C')
                print(f'High: {high} °C')
                print(f'Low: {low} °C')
                print(f'Description: {description}')
                print(f'Wind: {wind_speed} km/h')
                print(f'Pressure: {pressure} hPa')
                print(f'{city}, {state}, {postcode}, {country}')

    elif answer == 'kelvin' or answer == 'k':
        user_input = input('Please enter a city name, state or zipcode').lower()
        weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&zip={zip}&appid={API_KEY}')
        if weather_data.json()['cod'] == '404':
            print('No City found! Please enter full city and state name: ')
        else:
            # variables created from data that's pulled from api
            temp = round(weather_data.json()['main']['temp'])
            feels_like = round(weather_data.json()['main']['feels_like'])
            high = round(weather_data.json()['main']['temp_max'])
            low = round(weather_data.json()['main']['temp_min'])
            pressure = weather_data.json()['main']['pressure']
            description = weather_data.json()['weather'][0]['description']
            wind_speed = weather_data.json()['wind']['speed']
            geolocator = Nominatim(user_agent='WeatherProgram')
            lat = weather_data.json()['coord']['lat']
            lon = weather_data.json()['coord']['lon']
            location = geolocator.reverse(f'{lat},{lon}', language='en')
            location = location.raw['address']
            city = location['city']
            state = location['state']
            postcode = location['postcode']
            country = location['country']
            print(f'Kelvin: {temp} K')
            print(f'feels like: {feels_like} K')
            print(f'High: {high} K')
            print(f'Low: {low} K')
            print(f'Description: {description}')
            print(f'Wind: {wind_speed} km/h')
            print(f'Pressure: {pressure} hPa')
            print(f'{city}, {state}, {postcode}, {country}')
#main function calls our units_of_measurement function
def main():
    # Ask the user what unit of measurement they want until they enter it.
    while True:
        user_input2 = input('Kelvin(k), imperial(i), metric(m): ').lower()
        while user_input2 not in ['k', 'i', 'm','kelvin', 'metric', 'imperial']:
            user_input2 = input('Invalid please enter kelvin(k), imperial(i), metric(m): ').lower()
        # call our units_of_measurement in the main function
        units_of_measurement(answer=user_input2)
        #ask user if they want to continue the program
        continue_program = input("Do you want to continue? (y/n): ")
        if continue_program.lower() != 'y':
            break
if __name__ == '__main__':
    main()









