from playwright.sync_api import sync_playwright
import pandas as pd

def format_city(city):
    return city.replace(' ', '+')

city = input("Enter the city: ")
formatted_city = format_city(city)

titles = []
links = []
companies = []
locations = []

base_url = f'https://www.indeed.com/jobs?q=software+engineer&l={formatted_city}&sort=date&start='
base = 'https://indeed.com'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--lang=en-US'])
    page = browser.new_page()
    
    for start in range(0, 10, 10): 
        page_url = f"{base_url}{start}"
        page.goto(page_url, timeout=60000)
        page.wait_for_timeout(5000)
        
        titles_xpath = page.locator('//div[@class="job_seen_beacon"]//h2//span').all()
        links_xpath = page.locator('//div[@class="job_seen_beacon"]//h2/a').all()
        companies_xpath = page.locator('//span[@data-testid="company-name"]').all()
        locations_xpath = page.locator('//div[@data-testid="text-location"]').all()
        
        for title in titles_xpath:
            try:
                titles.append(title.inner_text())
            except:
                titles.append(None)
        
        for link in links_xpath:
            try:
                links.append(base + link.get_attribute('href'))
            except:
                links.append(None)
        
        for company in companies_xpath:
            try:
                companies.append(company.inner_text())
            except:
                companies.append(None)
        
        for location in locations_xpath:
            try:
                locations.append(location.inner_text())
            except:
                locations.append(None)
    
    browser.close()

map_data = {
    'Title': titles,
    'Company': companies,
    'Location': locations,
    'Link': links,
}

df = pd.DataFrame(map_data)
print(df)
df.to_excel('indeed_jobs.xlsx', index=False)
