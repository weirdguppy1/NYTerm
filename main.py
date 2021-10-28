import click
from BooksWidget import BooksWidget
from NewsWidget import NewsWidget

@click.command()
@click.argument('t', default='news.popular')
def main(t: str):
    """Interacts with the NYT news api. This project does not hold any 
    monetary value whatsoever. The author of this project is not 
    responsible for users that do not follow the NYT API Guidelines."""

    full_input = t.split('.')
    topic = full_input[0]
    section = full_input[1]
    print(topic, section)
    if(topic in ['books', 'b']):
        widget = BooksWidget()
        widget.showBox()
    elif(topic in ['news', 'n', 'newspaper']):
        widget = NewsWidget(section=section)
        widget.showBox()

    # widget = NewsWidget()
    # widget.showBox()


if __name__ == '__main__':
    main()
