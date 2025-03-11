import requests

# نام شهر و مختصات جغرافیایی آن (در اینجا برای مثال تهران)
latitude = 35.6892  # عرض جغرافیایی
longitude = 51.3890  # طول جغرافیایی

# URL درخواست برای دریافت وضعیت آب‌وهوا
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# ارسال درخواست به API
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data["current_weather"]["temperature"]
    wind_speed = data["current_weather"]["windspeed"]
    weather_code = data["current_weather"]["weathercode"]

    # تبدیل کد وضعیت آب‌وهوا به متن قابل فهم
    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Light snow",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Light rain showers",
        81: "Moderate rain showers",
        82: "Heavy rain showers",
        85: "Light snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with light hail",
        99: "Thunderstorm with heavy hail"
    }

    weather_description = weather_conditions.get(weather_code, "Unknown weather")

    print(f"وضعیت هوا: {weather_description}")
    print(f"دما: {temperature}°C")
    print(f"سرعت باد: {wind_speed} km/h")

else:
    print("خطا در دریافت داده‌ها!")
