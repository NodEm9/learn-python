from flask import Flask, render_template, request
from waitress import serve
from weather import get_current_weather


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def weather():
  city = request.args.get('city')
  weather_data = get_current_weather(city)
  return render_template('weather.html',
          title=weather_data['name'],
          temp=f"{weather_data['main']['temp']:.1f}",
          status=weather_data['weather'][0]['description'].capitalize(),
          feels_like=f"{weather_data['main']['feels_like']:.1f}",
          )



if __name__ == '__main__':
  serve(app, host='0.0.0.0', port=5000)
