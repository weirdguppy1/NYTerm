import click
from rich import print
from BooksWidget import BooksWidget
from NewsWidget import NewsWidget

@click.command()
@click.argument('t', default='news.popular')
def main(t: str):
    """Interacts with the NYT news api. This project does not hold any 
    monetary value whatsoever. The author of this project is not 
    responsible for users that do not follow the NYT API Guidelines."""
    if(t in ['books', 'b']):    
        widget = BooksWidget()
        widget.showBox()
        return

    if(t in ['news', 'n', 'newspaper']):
        widget = NewsWidget(section="popular")
        widget.showBox()   
        return 


    full_input = t.split('.')
    topic = full_input[0]
    section = full_input[1]
    
    if(topic in ['news', 'n', 'newspaper']):
        widget = NewsWidget(section=section)
        widget.showBox()
        return

    print("[red bold italic]The input is not recognized by the program![/]")
    # widget = NewsWidget()
    # widget.showBox()


if __name__ == '__main__':
    main()
