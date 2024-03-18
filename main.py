from flask import Flask, request, render_template
from weather_app import weather_responder 

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    return render_template("index.html")

@app.route("/weather")

def get_weather():
    city = request.args.get('city')
    weather_data = weather_responder(city)

    if not city or weather_data['cod'] == '404':
        return render_template("city_not_found_page.html")
    else:
        return render_template(
            "weather.html",
            title = weather_data['name'],
            status = weather_data['weather'][0]['description'],
            temp = weather_data['main']['temp']
        )
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)