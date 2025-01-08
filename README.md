# X (Twitter) Trending Topics Scraper

A web application that automatically scrapes and stores trending topics from X (formerly Twitter) using Selenium WebDriver and provides a clean interface to view the results.

## Features

- Automated login to X (Twitter) using Selenium
- Extracts top 4 trending topics
- Stores data in MongoDB with timestamp and IP address
- Web interface to view and trigger scraping
- Asynchronous scraping process
- Detailed logging

## Prerequisites

- Python 3.x
- Chrome Browser
- ChromeDriver (matching your Chrome version)
- MongoDB Atlas account

## Installation

1. Clone this repository
2. Install required packages:
   bash
   pip install -r requirements.txt
   
3. Configure the following variables in selenium_script.py:
   - TWITTER_USERNAME
   - TWITTER_PASSWORD
   - TWITTER_EMAIL
   - CHROME_DRIVER_PATH
   - MONGO_URI

## Project Structure

- app.py - Flask web server implementation
- selenium_script.py - Core scraping functionality using Selenium
- index.html - Frontend interface
- requirements.txt - Python dependencies
- fetch_proxy.py - Proxy configuration (if needed)

## Usage

1. Start the Flask server:
   bash
   python app.py
   
2. Open a web browser and navigate to http://localhost:5000
3. Click the "Fetch Trending Topics" button to start scraping

## Data Storage

The application stores the following information in MongoDB:
- Unique ID for each scrape
- Four trending topics
- Timestamp
- IP address used for scraping

## Technical Details

- Built with Flask for the backend server
- Uses Selenium WebDriver for web scraping
- MongoDB Atlas for data persistence
- Threading implementation for non-blocking scraping operations
- Error handling and logging mechanisms

## Security Note

Please ensure to keep your credentials secure and never commit them directly in the code. Consider using environment variables for sensitive information.
