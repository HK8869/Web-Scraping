import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = https://www.accuweather.com/

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML elements containing the article titles (adjust as needed)
        article_titles = soup.find_all('h2', class_='article-title')

        # Loop through the article titles and print them
        for title in article_titles:
            print(title.text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
