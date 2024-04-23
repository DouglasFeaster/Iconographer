from PIL import Image
import click
from pathlib import PurePath
import os
import datetime


sizes = [16, 24, 32, 48, 64, 128, 256]

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

@click.command()
@click.argument('src', type=click.Path(exists=True))
# @click.argument('dst', nargs=1, type=click.Path(exists=True))
@click.option('--ico', is_flag=True, show_default=True, default=False, type=bool, help='Generate ICO files.')
@click.option('--png', is_flag=True, show_default=True, default=False, type=bool, help='Generate PNG files.')
def do_work(src, ico, png):
    
    output_dir = "icons"

    img = Image.open(src)

    filename = PurePath(src).stem
    os.mkdir(output_dir)

    for size in sizes:
        img2 = img.resize((size, size))

        if ico:
            img2.save(f"./{output_dir}/{size}x{size}.ico")
            click.echo(f"{size}x{size}.ico Created!")

        if png:
            img2.save(f"./{output_dir}/{size}x{size}.png")
            click.echo(f"{size}x{size}.png Created!")


if __name__ == '__main__':
    do_work()