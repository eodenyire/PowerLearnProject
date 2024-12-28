# Weather App

A simple weather application that allows users to search for the current weather in any city using the OpenWeather API. The app provides the city's name, country, date, temperature, and weather description. The weather data is fetched using the OpenWeather API and displayed in a user-friendly interface.

## Features

- Search for weather by city name.
- Displays the current temperature in Celsius.
- Shows a weather description (e.g., clear sky, clouds, etc.).
- Dynamic date display.
- Simple and clean user interface with responsive design.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **API**: OpenWeather API (for fetching weather data)
- **External Libraries**: Font Awesome (for search icon), Google Fonts (for custom fonts)

## Screenshots

![Weather App Screenshot](./weather-screenshot.jpg)

---

## Project Setup

### Prerequisites

- **OpenWeather API Key**: You need to sign up on [OpenWeather](https://openweathermap.org/) to get an API key. Once you have the key, you can integrate it into the app.
  
- **Code Editor**: Any text editor of your choice (e.g., Visual Studio Code, Sublime Text, etc.)

---

### Getting Started

1. **Clone the repository**:
   Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
# Weather App Setup and Instructions

## Obtain an API key from OpenWeather:
1. Visit [OpenWeather](https://openweathermap.org/api) to get your API key.
2. Replace the `YOUR_API_KEY` in `script.js` with your actual API key.

## Open the project:
1. Open the `index.html` file in your browser to view the Weather App.

---

## File Structure


---

## Code Explanation

### `index.html`
This file contains the structure of the weather application. It includes:
- An input field for entering a city.
- A button to trigger the search.
- Sections to display the weather data.
- Font Awesome icons are used for the search button.

### `script.js`
This file contains the core functionality:
- **API Request**: When the user clicks the search button, an API request is made to OpenWeather using the city entered by the user.
- **Weather Data Display**: The weather data (city, country, date, temperature, and description) is displayed dynamically on the page.
- **Error Handling**: If the user enters an invalid city name or if there's an issue with the API request, an error message is shown.

### `style.css`
The styles are applied to make the app visually appealing:
- **Responsive Design**: The app layout is optimized for various screen sizes.
- **Weather Display**: The weather data is shown with bold fonts and eye-catching colors.

---

## How to Use

### Search for Weather:
1. Type a city name into the search box (e.g., "London").
2. Click the search button or press "Enter".
3. The weather data for the city will be displayed, including the temperature and weather description.

### Customize the App:
- You can modify the app's style in `style.css` to fit your design preferences.
- You can also enhance the functionality, such as adding support for multiple cities, temperature unit conversions (Celsius/Fahrenheit), or even a 7-day forecast.

---

## Contribution

1. Fork the repository to make your changes.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature

