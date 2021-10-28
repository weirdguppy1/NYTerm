from Widget import Widget
from rich.layout import Layout
from rich.console import Console
from rich.panel import Panel

class WidgetLayout:

    def __init__(self, one: Widget, two: Widget, three: Widget, four: Widget) -> None:
        
        self.layout = Layout()
        self.layout.split_column(
            Layout(name="upper"),
            Layout(name="lower")
        )
        self.layout["upper"].split_row(
            Layout(Panel(one), name=1),
            Layout(Panel(two), name=2),
        )
        self.layout["lower"].split_row(
            Layout(Panel(three), name=3),
            Layout(Panel(four), name=4)
        )


    def show(self):
        console = Console()
        console.print(self.layout)

    def configureLayout(self):
        self.layout.split_column()


layout = WidgetLayout()

layout.show()