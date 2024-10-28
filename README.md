# Weather App 🌦️

A simple Django-based weather application that fetches and displays weather data for cities using the OpenWeatherMap API. This project was developed to showcase skills in web development with Django and API integration.

## Features
- Displays weather details including temperature, humidity, description, wind speed, and geographical coordinates.
- Converts temperature to Celsius and Fahrenheit.
- Provides feedback for invalid city names with a user-friendly error message.

## Project Structure

- **templates/**: Contains the HTML templates (mainly `weather.html`) for the app.
- **weather/**: Includes Django views and other backend functionality.
- **manage.py**: Django's command-line utility for administrative tasks.

## Live Demo

Check out the live demo of the app here:
[**Live Weather App**](https://your-live-deployment-link.com) 

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Madhu65498721/Weather-App.git
   ```
2. Navigate into the project directory:
   ```bash
   cd weatherapp
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables for your OpenWeatherMap API key:
   - Create a `.env` file in the root of your project.
   - Add your API key:
     ```
     OPENWEATHERMAP_API_KEY=your_api_key_here
     ```
5. Run the Django server:
   ```bash
   python manage.py runserver
   ```
6. Visit `http://127.0.0.1:8000` in your browser to view the app.

## Usage

- Enter a city name in the search bar and press enter.
- If the city name is valid, the weather information for the city will be displayed.
- If the city name is invalid, an error message will prompt you to enter a valid city name.

