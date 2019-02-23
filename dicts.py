cities_temperature = {"city": "Москва", "temperature": "20"}
print(cities_temperature['city'])
cities_temperature["temperature"] = int(cities_temperature["temperature"]) - 5
print(cities_temperature)

print(cities_temperature.get("country"))
cities_temperature.get("country", 'Россия')
#cities_temperature["country"] = "Россия"
cities_temperature["date"] = '27.05.2019'
print(cities_temperature)