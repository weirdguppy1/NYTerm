from rich.panel import Panel
from rich.console import Console


class Widget:
    def __init__(self, title: str, description: str, footer="") -> None:
        self.title = title
        self.description = description
        self.footer = footer

    def _content(self) -> str:
        return ""

    def showBox(self):
        console = Console()
        text = f"""[bold red]{self.title}[/bold red]\n{self.description}\n\n{self._content()}\n-\n[italic blue]{self.footer}[/italic blue]"""        
        group = Panel(text, expand=True)
        console.print(group)
        