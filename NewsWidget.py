from rich.console import Console
from rich.panel import Panel
from Widget import Widget
from config import API_KEY
import requests
import json

class NewsWidget(Widget):
    def __init__(self, section="popular") -> None:
        self.title = f"{section.capitalize()} News"
        self.description = f"{section.capitalize()} news from NYT."
        self.footer = "Made by: weirdguppy1"
        self.section = section

    def _showList(self, data):
        text = ""
        for article in data['results'][:5]:
            text+=f"[cyan]{article['title']}[/]\n[yellow]{article['abstract']}[/]\nLink: {article['url']}"
            text+="\n\n"
        return text

    def _showPopularNews(self) -> str:
        data = json.loads(requests.get(f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?&api-key={API_KEY}').text)
        return self._showList(data)

    def _showSection(self, section) -> str:
        data = json.loads(requests.get(f' https://api.nytimes.com/svc/topstories/v2/{section}.json?&api-key={API_KEY}').text)
        return self._showList(data)

    def _content(self) -> str:
        if(self.section in ['world', 'politics', 'us', 'science', 'business']):
            return self._showSection(self.section)
        return self._showPopularNews()

    # def showBox(self):
    #     console = Console()
    #     text = f"""[bold red]{self.title}[/bold red]\n{self.description}\n\n{self._content()}\n-\n[italic blue]{self.footer}[/italic blue]"""
    #     group = Panel(text, expand=True)
    #     console.print(group)
        
