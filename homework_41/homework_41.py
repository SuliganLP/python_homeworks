import pymysql
import os
from dotenv import load_dotenv

load_dotenv(".env")

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_DATABASE', 'test'),
}

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT name FROM country')

        for num, country in enumerate(cursor.fetchall(), 1):
            print(f"{num}. {country[0]}")

        user_country = input("Enter country name or country number: ").strip()

        if user_country.isdigit():
            user_country = int(user_country)
            cursor.execute("SELECT name FROM country")
            for num, country in enumerate(cursor.fetchall(), 1):
                if user_country == num:
                    user_country = country[0]
                    break

        cursor.execute("SELECT Code FROM country WHERE Name =%s", (user_country,))
        country_code = cursor.fetchone()

        cursor.execute("SELECT Name, Population FROM city WHERE CountryCode = %s", (country_code,))
        for num, city in enumerate(cursor.fetchall(), 1):
            print(f"{num}. {city[0]} - {city[1]}")
