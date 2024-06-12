# Food Items Scraper

This repository contains a Python script to scrape the food menu and price details from a [Magicpin restaurant page](https://magicpin.in/New-Delhi/Sunehri-Bagh-Road-Area/Restaurant/AuntyS-Kitchen/store/515832/delivery/) using Selenium and BeautifulSoup.

## Description

The script uses Selenium WebDriver to interact with the Magicpin restaurant webpage. It extracts the food menu items and their respective prices, even handling dynamically loaded content by clicking on "show more" buttons to reveal hidden items. BeautifulSoup is used to parse the HTML content and extract the relevant details.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- Chrome WebDriver

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Food-items-scraper.git
   cd Food-items-scraper
   ```

2. **Install the required Python libraries:**

   ```bash
   pip install selenium beautifulsoup4
   ```

3. **Download Chrome WebDriver:**

   Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it matches your installed version of Chrome. Place the `chromedriver` executable in a known location.

## Usage

1. **Update the script:**

   In the `scraper.py` file, update the `service` path to point to your `chromedriver` executable:

   ```python
   service = Service("/path/to/chromedriver")  # Update this with the path to your ChromeDriver
   ```

2. **Run the script:**

   ```bash
   python task_1.py
   ```

3. **Output:**

   The script will output the food menu items and their prices with numbering.

## Example

An example of the script output:

```
1. Name: 2 Mix Paratha With Curd, Price: ₹120
2. Name: Paneer Butter Masala, Price: ₹250
3. Name: Chicken Biryani, Price: ₹350
...
```



### Notes:
- Adjust the repository URL (`https://github.com/yourusername/Food-items-scraper.git`) and any other placeholders as necessary.
- Ensure the `service` path in the Python script points to the correct location of your `chromedriver` executable.
