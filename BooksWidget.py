from rich.console import Console
from Widget import Widget
from config import API_KEY
import requests
import json
from rich.panel import Panel

class BooksWidget(Widget):
    def __init__(self) -> None:
        self.title = "Books"
        self.description = "Popular books reviewed by NYT."
        self.footer = "Made by: weirdguppy1"

    def _showList(self, data):
        text = ""
        for article in data['results']['books'][:5]:
            text+=f"[cyan]{article['title']} By: {article['author']}[/]\n[yellow]{article['description']}[/]\nLink: {article['amazon_product_url']}"
            text+="\n\n"
        return text

    def _showPopularBooks(self) -> str:
        data = json.loads(requests.get(f' https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?&api-key={API_KEY}').text)
        return self._showList(data)
        
    def _content(self) -> str:
        return self._showPopularBooks()

        
         
