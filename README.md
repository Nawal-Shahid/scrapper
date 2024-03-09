
# Web Scraper Application Documentation

This Python application utilizes PyQt5 and BeautifulSoup to create a simple web scraper. The application allows users to enter a URL, scrape the content from the specified webpage, and view the results. Additionally, users can save the scraped data to a text file.


## Requirements
- Python 3.x
- PyQt5
- requests
- BeautifulSoup
## Usage/Examples

1. **Run the Application:**
   - Execute the script in a Python environment to launch the web scraper application.

2. **Enter URL:**
   - Input the URL of the webpage you want to scrape in the provided text field.

3. **Scrape:**
   - Click the "Scrape" button to fetch and display the content from the specified webpage.

4. **View Results:**
   - The results will be displayed in the text browser.

5. **Save to File:**
   - Click the "Save to File" button to save the scraped content to a text file. Choose the desired location and file name through the file dialog.

## Code Structure

The code consists of a PyQt5 GUI with the following components:

- **URL Input Field:** Allows users to enter the URL of the webpage to be scraped.
- **Scrape Button:** Initiates the web scraping process when clicked.
- **Text Browser:** Displays the scraped content or error messages.
- **Save to File Button:** Saves the scraped data to a user-specified text file.
## Dependencies
- `PyQt5`: Provides the graphical user interface components.
- `requests`: Handles HTTP requests to fetch webpage content.
- `BeautifulSoup`: Parses HTML content for data extraction.
## How To Run
Execute the script in a Python environment. The application window will appear, allowing users to interact with the web scraper.
## Author & Author's Note

[@Nawal-Shahid](https://github.com/Nawal-Shahid)


- Ensure a stable internet connection for successful web scraping.
- The application utilizes the `requests` library for fetching webpage content and `BeautifulSoup` for HTML parsing.

Enjoy exploring and scraping web content with this simple PyQt5-based web scraper application!