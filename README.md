# Web Scraping Shopify Website Services in the UK

This project aims to scrape data from websites of companies offering Shopify website services in the UK. The data collected includes the company name, category, location, opening time, and website URL.

## Tools Used
- **Selenium**: Used to automate web browser interaction and data extraction.
- **Python**: Programming language used to write the scraping script.
- **ChromeDriver**: WebDriver used by Selenium for browser automation.

## Process Overview
1. **Setup**: Install necessary libraries (`selenium`, `webdriver_manager`) and ensure Python environment is configured.

2. **Selenium Configuration**: Set up Selenium with ChromeDriver to automate web browsing.

3. **Scraping Process**:
   - Navigate to the target websites of companies offering Shopify services.
   - Use Selenium to interact with the web pages, locating and extracting relevant data such as company name, category, location, opening time, and website URL.
   - Handle any dynamic content loaded via JavaScript using Selenium's capabilities.

4. **Data Collection**: Store the scraped data in appropriate data structures (lists, dictionaries) within the Python script.

5. **Data Export**: Write the collected data to a text file for further analysis or use. 

## File Structure
- `web.py`: Python script containing the scraping logic.
- `webdesigners.txt`: Text file where the scraped data is stored.

## Running the Script
1. Clone the repository to your local machine.
2. Install the required Python libraries: `pip install selenium webdriver_manager`.
3. Ensure you have the latest version of Chrome installed.
4. Run the `web.py` script.
5. Once the scraping process is complete, check the `webdesigners.txt` file for the extracted data.

## Important Notes
- **Ethical Use**: Ensure compliance with the terms of service of the websites being scraped. Respect robots.txt directives and avoid causing unnecessary strain on the target server.
- **Data Accuracy**: While efforts have been made to ensure the accuracy of the scraped data, manual verification may be necessary for critical applications.

## Disclaimer
This project is for educational and informational purposes only. The author does not endorse or encourage unauthorized scraping of websites. 


### website view

![image](https://github.com/FaeyO/webscrapping-companies-offereing-shopify-website-service/assets/118575325/5be7f2e6-ee93-494d-a179-d9ae21b199a3)
