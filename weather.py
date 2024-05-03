import requests
from db import create_database, add_to_database, get_all_data_from_database
from objects import WeatherData

def get_weather(city):
    api_key = '6277c7ffa29b0961665066e5b23c9d41'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = f"{base_url}q={city}&appid={api_key}&units=imperial"

    response = requests.get(complete_url)
    data = response.json()

        #print("API Response:", data) Uncomment this to view full API response

    if data.get("cod") == 200:
        try:
            main_data = data['main']
            weather = data['weather'][0]

            temperature = main_data['temp']
            description = weather['description']

            print(f"Weather in {city}: {description}, Temperature: {temperature}°F")
            return WeatherData(city, description, temperature)
        except KeyError as e:
            print(f"Error: KeyError - {e}. The structure of the response might have changed.")
            return None
    else:
        print("City not found or API request failed.")
        return None


def display_data(data):
    if data:
        print("Weather Data:")
        for row in data:
            print(row)
    else:
        print("No data found.")

def menu():
    print("1. Get Weather")
    print("2. Display Database")
    print("3. Exit")

def main():
    create_database()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            city_input = input("Enter city name: ")
            weather_data = get_weather(city_input)
            if weather_data:
                add_to_database(weather_data)
        elif choice == '2':
            data = get_all_data_from_database()
            display_data(data)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
