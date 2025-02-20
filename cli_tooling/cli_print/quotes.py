import random # Python Standard Library
import requests # Pip installed packages
from bs4 import BeautifulSoup # Pip installed packages

# URL to scrape
url = "https://quotes.toscrape.com"

def get_soup():

    # Fetch the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return soup

def scrape_quote(quote_container):
    
    quote = quote_container.find(
        'span',
        {'class': 'text'}
        ).text
    
    author = quote_container.find(
        'small',
        {'class': 'author'}
        ).text
    
    return {
        'quote': quote,
        'author': author
        } 

def main():
    
    soup = get_soup()
    
    # Extract data
    quotes = [
        scrape_quote(div) 
        for div in soup.find_all('div', {'class': 'quote'})
        ]

    # Select random quote
    quote = random.choice(quotes)

    # Print quote
    print('\033[1m')
    print(quote['quote'])
    print('\33[35m')
    print('-', quote['author'])
    print('\033[0m')
    
if __name__ == "__main__":
    main()
