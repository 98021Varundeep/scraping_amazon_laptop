# Amazon Product Scraper

![Amazon](https://img.shields.io/badge/Amazon-Scraper-brightgreen)

## 📊 Overview

The Amazon Product Scraper is a powerful tool for extracting product information from Amazon search results pages. By leveraging BeautifulSoup and Selenium, this project allows you to collect essential product details such as titles, prices, and links. The data is neatly organized and saved into a CSV file for easy analysis.

## 🗂️ Project Structure

- **`scraper.py`**: Extracts product details from saved HTML files and saves them into a CSV file.
- **`selenium_scraper.py`**: Automates browser navigation to fetch and save HTML content from Amazon search results.
- **`python_website_scraper.py`**: Demonstrates basic web scraping using Selenium on the Python official website.
- **`data/`**: Directory where HTML files are stored.
- **`data.csv`**: CSV file containing the extracted product data.

## 🛠️ Requirements

To run the project, you'll need:

- **`Python 3.x`**
- **`BeautifulSoup 4`**
- **`Pandas`**
- **`Selenium`**
- **`ChromeDriver`**

Install the required Python libraries using:
 pip install beautifulsoup4 pandas selenium

 Download ChromeDriver from ChromeDriver download page and ensure it's added to your system's PATH.

## ⚙️ Setup
 Create Directory: Ensure a directory named data/ exists in the project root. This is where HTML files will be saved.

 -Install Dependencies: Use pip to install the necessary libraries:
    pip install beautifulsoup4 pandas selenium

  ChromeDriver Setup: Download and install ChromeDriver, and make sure it is included in your PATH.

## 🚀 Usage
 1. Extract Product Information
 Run the following command to parse HTML files and extract product details:
 python scraper.py

2. Fetch and Save HTML Content
 To automate fetching HTML content from Amazon search results, execute:
 python selenium_scraper.py

3. Basic Web Scraping Example
 python python_website_scraper.py

## ⚠️ Notes
 Ensure compliance with Amazon’s terms of service when scraping their site.
 Adjust time.sleep() intervals to manage scraping rate and avoid throttling.
## 📜 License
 This project is licensed under the MIT License. See the LICENSE file for details.

## 🙌 Acknowledgments
BeautifulSoup for HTML parsing.
Selenium for browser automation.
ChromeDriver for controlling Chrome.
