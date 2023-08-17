
# SeamsFriendly Website Scraper for Boxers

The SeamsFriendly Website Scraper is a Python-based web scraping tool built using the Scrapy framework. This scraper is designed to gather information about boxers from a target website and store the collected data for further analysis or use. The tool utilizes Scrapy's powerful features to efficiently navigate through web pages, extract relevant information, and organize it into a structured format.

## Features

- **Efficient Scraping**: The scraper uses asynchronous requests and concurrent processing, making the scraping process fast and efficient.

- **Customizable Configuration**: The scraper's settings can be easily customized to adapt to changes in the website structure or to fine-tune the scraping behavior.

- **Data Persistence**: Collected data is stored in a structured format (such as JSON or CSV) for easy access and analysis.

- **User-Friendly**: The scraper is built with simplicity in mind, making it easy to understand and modify according to your needs.

## Prerequisites

Before using the SeamsFriendly Website Scraper, ensure you have the following components installed:

- Python 3.x
- Scrapy library (`pip install scrapy`)

## Usage

1. **Clone the Repository**:
   Clone this repository to your local machine using Git:

   ```
   git clone https://github.com/Tejas-Samel/Scraping-SeamsFriendly.git
   ```

2. **Navigate to the Project Directory**:
   Move into the project directory:

   ```
   cd seamsfriendly-boxer-scraper
   ```

3. **Configure the Scraper**:
   Open the `settings.py` file and customize the scraping settings to fit the target website's structure:

   ```python
   # Set the target website URL
   START_URL = '"https://in.seamsfriendly.com/collections/shorts/?page=1'

   # Configure User-Agent to mimic a real browser
   USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
   ```

4. **Run the Scraper**:
   Run the scraper using the following command:

   ```
   scrapy crawl quotes
   ```

   The scraper will start navigating the target website, extracting boxer information, and storing it in the specified output format (e.g., JSON or CSV).

5. **Retrieve the Data**:
   Once the scraping process is complete, you will find the collected data in the output file you configured in `settings.py`.
