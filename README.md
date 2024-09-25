# Indeed Job Scraper

This project is a web scraper that extracts job listings from Indeed based on a specified city. The script uses Playwright to navigate through the job listings and Pandas to store the data in an Excel file.

## Requirements

- Python 3.7+
- Playwright
- Pandas
- Openpyxl

## Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/mykolamyronenko/IndeedScraper.git
    cd IndeedScraper
    ```

2. **Create a virtual environment:**
   ```
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
      ```
      .venv\Scripts\activate
      ```

   - On macOS/Linux:
      ```
      source .venv/bin/activate
      ```
   
4. **Activate the virtual environment:**
    ```  
    pip install -r requirements.txt 
    ```
   
5. **Install browser:**
    ```  
    playwright install chromium
    ```

## Usage

1. **Run the script:**

    ```
    python main.py
    ```

2. **Enter the city name when prompted:**

    The script will ask you to enter the city name. If the city name contains two or more words, they should be separated by spaces (e.g., `New York`).

3. **Output:**

    The script will generate an Excel file named `indeed_jobs.xlsx` containing the following columns:
    - Title
    - Company
    - Location
    - Link


## Notes

- Adjust the range in the `for start in range(0, 200, 10)` line to cover the number of pages you want to scrape.
- The script currently runs in non-headless mode (`headless=False`). 


