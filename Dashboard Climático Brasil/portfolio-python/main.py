from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__, template_folder="templates")

# OpenWeatherMap API Configuration
OPENWEATHER_API_KEY = ""  # SEU TOKEN AQUI
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"

STATES_CITIES = {
    "Acre": ["Rio Branco", "Cruzeiro do Sul", "Sena Madureira"],
    "Alagoas": ["Maceió", "Arapiraca", "Rio Largo"],
    "Amapá": ["Macapá", "Santana", "Oiapoque"],
    "Amazonas": ["Manaus", "Parintins", "Itacoatiara"],
    "Bahia": ["Salvador", "Feira de Santana", "Vitória da Conquista"],
    "Ceará": ["Fortaleza", "Caucaia", "Juazeiro do Norte"],
    "Distrito Federal": ["Brasília", "Taguatinga", "Ceilândia"],
    "Espírito Santo": ["Vitória", "Vila Velha", "Serra"],
    "Goiás": ["Goiânia", "Anápolis", "Aparecida de Goiânia"],
    "Maranhão": ["São Luís", "Imperatriz", "Caxias"],
    "Mato Grosso": ["Cuiabá", "Várzea Grande", "Rondonópolis"],
    "Mato Grosso do Sul": ["Campo Grande", "Dourados", "Três Lagoas"],
    "Minas Gerais": ["Belo Horizonte", "Uberlândia", "Contagem"],
    "Pará": ["Belém", "Ananindeua", "Santarém"],
    "Paraíba": ["João Pessoa", "Campina Grande", "Patos"],
    "Paraná": ["Curitiba", "Londrina", "Maringá"],
    "Pernambuco": ["Recife", "Jaboatão dos Guararapes", "Olinda"],
    "Piauí": ["Teresina", "Parnaíba", "Picos"],
    "Rio de Janeiro": ["Rio de Janeiro", "Niterói", "Duque de Caxias"],
    "Rio Grande do Norte": ["Natal", "Mossoró", "Parnamirim"],
    "Rio Grande do Sul": ["Porto Alegre", "Caxias do Sul", "Pelotas"],
    "Rondônia": ["Porto Velho", "Ji-Paraná", "Ariquemes"],
    "Roraima": ["Boa Vista", "Rorainópolis", "Caracaraí"],
    "Santa Catarina": ["Florianópolis", "Blumenau", "Joinville"],
    "São Paulo": ["São Paulo", "Campinas", "Santos"],
    "Sergipe": ["Aracaju", "Nossa Senhora do Socorro", "Lagarto"],
    "Tocantins": ["Palmas", "Araguaína", "Gurupi"],
}


def get_current_weather(city_name):
    try:
        url = f"{OPENWEATHER_BASE_URL}/weather"
        params = {
            "q": city_name,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": "pt_br",
        }
        response = requests.get(url, params=params, timeout=5)

        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temp": round(data["main"]["temp"], 1),
                "humidity": round(data["main"]["humidity"], 1),
                "pressure": round(data["main"]["pressure"], 1),
                "wind": round(data["wind"]["speed"], 1),
                "condition": data["weather"][0]["main"],
                "description": data["weather"][0]["description"].capitalize(),
                "success": True,
            }
        return {"success": False}
    except Exception as e:
        print(f"Erro ao buscar clima atual de {city_name}: {e}")
        return {"success": False}


def get_forecast(city_name):
    try:
        url = f"{OPENWEATHER_BASE_URL}/forecast"
        params = {
            "q": city_name,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": "pt_br",
        }
        response = requests.get(url, params=params, timeout=5)

        if response.status_code == 200:
            data = response.json()
            weather_emojis = {
                "Clear": "☀️",
                "Clouds": "☁️",
                "Rain": "🌧️",
                "Drizzle": "🌦️",
                "Thunderstorm": "⛈️",
                "Snow": "❄️",
                "Mist": "🌫️",
                "Smoke": "💨",
                "Haze": "🌫️",
                "Dust": "🌪️",
                "Fog": "🌫️",
                "Sand": "🌪️",
                "Ash": "💨",
                "Squall": "💨",
                "Tornado": "🌪️",
            }

            hours = []
            temps = []
            humidity = []
            conditions = []

            for item in data["list"][:8]:
                dt = datetime.fromtimestamp(item["dt"])
                hours.append(dt.strftime("%H:00"))
                temps.append(round(item["main"]["temp"], 1))
                humidity.append(round(item["main"]["humidity"], 1))
                main_condition = item["weather"][0]["main"]
                emoji = weather_emojis.get(main_condition, "🌤️")
                description = item["weather"][0]["description"].capitalize()
                conditions.append(f"{emoji} {description}")

            return {
                "city": data["city"]["name"],
                "hours": hours,
                "temps": temps,
                "humidity": humidity,
                "conditions": conditions,
                "success": True,
            }
        return {"success": False}
    except Exception as e:
        print(f"Erro ao buscar previsão de {city_name}: {e}")
        return {"success": False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/states")
def api_states():
    return jsonify(list(STATES_CITIES.keys()))


@app.route("/api/cities/<state>")
def api_cities(state):
    cities = STATES_CITIES.get(state, [])
    return jsonify(cities)


@app.route("/api/city/<city>")
def api_city(city):
    weather = get_current_weather(city)
    if weather.get("success"):
        return jsonify(weather)
    return jsonify({"error": f"Não foi possível buscar dados de {city}"}), 400


@app.route("/api/forecast/<city>")
def api_forecast(city):
    forecast = get_forecast(city)
    if forecast.get("success"):
        return jsonify(forecast)
    return jsonify({"error": f"Não foi possível buscar previsão de {city}"}), 400


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🌤️  Dashboard Climático - Servidor Iniciado")
    print("=" * 60)
    print("\n📊 Acesse em: http://localhost:5000")
    print("\n💡 Dica: Use Ctrl+C para parar\n")
    app.run(debug=True, port=5000)
