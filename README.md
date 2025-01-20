# Company URL Scraper

**Company URL Scraper** is a Python script that automates the process of searching for company URLs from their names stored in an Excel file. It uses web scraping techniques to retrieve the official website URLs and saves the results back into the same Excel file. The script incorporates various precautions to bypass anti-bot protections, such as rotating user agents, using proxies, and adding random delays between requests.

## Features
- Reads company names from an Excel file.
- Searches for official websites using Google (can be adapted for other search engines).
- Rotates user agents and proxies to prevent blocking.
- Random delays between requests to simulate human behavior.
- Saves the resulting URLs in the same Excel file.

## Prerequisites
Before running the script, you need to install the following Python libraries:

- pandas
- requests
- beautifulsoup4
- fake_useragent
- openpyxl
- requests-ip-rotator

You can install them using `pip`:

