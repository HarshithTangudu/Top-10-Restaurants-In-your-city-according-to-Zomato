# Top 10 Restaurants Finder According to Zomato

## Overview

**Top 10 Restaurants Finder** is a simple yet powerful Python project that allows users to discover the best dining options in their city! Utilizing the Zomato API through web scraping, this project fetches the top 10 restaurants based on user input and generates an easily accessible Excel file with the restaurant names and their ratings.

## Features

- **User-Friendly**: Just input the city name, and the application takes care of the rest.
- **Data Export**: Automatically creates an Excel file containing the names and ratings of the top 10 restaurants in your specified city.
- **Real-Time Information**: Retrieves live data directly from Zomato, ensuring you always have the latest restaurant recommendations.

## Technologies Used

- **Python**: The core language for implementing the logic.
- **Beautiful Soup**: For parsing HTML and extracting restaurant data.
- **Requests**: For making HTTP requests to the Zomato website.
- **Pandas**: For data manipulation and exporting to Excel.

## How It Works

1. The user is prompted to enter a city name.
2. The application constructs the URL to access the Zomato best restaurants page for that city.
3. It sends a GET request to the URL, retrieves the HTML content, and parses it using Beautiful Soup.
4. The project collects the names and ratings of the top 10 restaurants.
5. Finally, the data is stored in an Excel file named *"Top 10 Restaurants in [City Name] According to Zomato.xlsx"*.

## Getting Started

### Prerequisites

- Python installed on your system.
- Required Python libraries: `requests`, `beautifulsoup4`, `pandas`.

### Installation

1. Clone the repository or download the files.
   ```bash
   git clone https://github.com/yourusername/top-10-restaurants-finder.git
   cd top-10-restaurants-finder
   ```

2. Install the required libraries.
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl
   ```

### Usage

1. Run the script:
   ```bash
   python top_10_restaurants.py
   ```
   
2. When prompted, enter your desired city name.

3. Check the generated Excel file for the top 10 restaurants!

## Example

```python
Enter your city name: Hyderabad
```

After executing the above command, you will find an Excel file named *"Top 10 Restaurants in Hyderabad According to Zomato.xlsx"* in your project directory.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.



## Acknowledgments

- [Zomato](https://www.zomato.com/) for providing the restaurant data.

