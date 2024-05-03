import sqlite3
from objects import WeatherData

def create_database():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS WeatherData 
                 (City TEXT, Description TEXT, Temperature REAL)''')

    conn.commit()
    conn.close()

def add_to_database(weather_data):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    c.execute("INSERT INTO WeatherData VALUES (?, ?, ?)", (weather_data.city, weather_data.description, weather_data.temperature))

    conn.commit()
    conn.close()

def get_all_data_from_database():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    c.execute("SELECT * FROM WeatherData")
    data = c.fetchall()

    conn.close()

    return data
