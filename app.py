import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.secret_key = 'your_secret_key'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = []

    if request.method == 'POST':
        new_city = request.form.get('city')
        
        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    for city in cities:
        try:
            r = requests.get(url.format(city.name)).json()

            # Check if 'main' key exists in the response
            if 'main' in r:
                city_name = city.name.capitalize()
                temperature_fahrenheit = r['main']['temp']
                temperature_celsius = round((temperature_fahrenheit - 32) * 5 / 9)
                country_code = r['sys']['country']

                weather = {
                    'city': f"{city_name}, {country_code}",
                    'temperature': temperature_celsius,
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                }

                weather_data.append(weather)
            else:
                print(f"Key 'main' not found in API response for city {city.name}")
                flash(f"No weather data found for {city.name}.", 'error')
                db.session.delete(city)
                db.session.commit()
        except Exception as e:
            print(f"Error processing data for city {city.name}: {e}")
            flash(f"Error processing data for city {city.name}: {e}")
    


    return render_template('weather.html', weather_data=weather_data)

@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/clear', methods=['POST'])
def clear_cities():
    #delete all entries from the City table
    db.session.query(City).delete()
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
   app.run(debug=True)
