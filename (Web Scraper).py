import requests
from bs4 import BeautifulSoup
import csv

def scrape_data():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    items = soup.find_all('article', class_='product_pod')
    
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Price'])
        
        for item in items:
            title = item.h3.a['title']
            price = item.find('p', class_='price_color').text
            writer.writerow([title, price])
            
    print("Scraping complete. Data saved to scraped_data.csv.")

if __name__ == "__main__":
    scrape_data()