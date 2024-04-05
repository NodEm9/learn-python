from flask import Flask, render_template, request
from waitress import serve
from weather import get_current_weather


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
  city = request.args.get('city')

#  If the city is empty or with tab spaces, set it to default Gelsenkirchen
  if not bool(city.strip()):
      city = "Gelsenkirchen"
         
  weather_data = get_current_weather(city)

  # City not found in the API   
  if not weather_data['cod'] == 200:
      return render_template('not-found.html')
          
        
  return render_template('weather.html',
          title=weather_data['name'],
          temp=f"{weather_data['main']['temp']:.1f}",
          status=weather_data['weather'][0]['description'].capitalize(),
          feels_like=f"{weather_data['main']['feels_like']:.1f}",
          )



if __name__ == '__main__':
  serve(app, host='0.0.0.0', port=5000)
