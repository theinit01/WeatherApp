# Weather App

This is a simple Flask web application for checking the weather of various cities around the world. Users can add cities to view current weather conditions, including temperature, description, and weather icon.

## Features

- **Add Cities:** Users can input the name of a city and add it to the list of cities displayed on the homepage.
- **Display Weather Information:** The app retrieves weather data from the OpenWeatherMap API and displays it for each city, including temperature in Celsius, description of weather condition, and an icon representing the weather.
- **Error Handling:** If a city is not found or if there is an error retrieving its weather data, the app will display an error message and remove the city from the list.

## Screenshots

<img src="https://github.com/theinit01/WeatherApp/blob/main/assets/Screenshot%202024-03-30%20174201.png">
<img src="https://github.com/theinit01/WeatherApp/blob/main/assets/Screenshot%202024-03-30%20174243.png">

## Usage

1. Clone the repository: `git clone https://github.com/yourusername/your-repo.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run `init_db.py` to create the necessary tables.
4. Run the application: `python app.py`
5. Access the app in your web browser at `http://localhost:5000`

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the Apache - see the [LICENSE](LICENSE) file for details.
