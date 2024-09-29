from rich import print
from typer import Typer

epilog = "For more information, visit https://github.com/thenerdlygentleman/photoalbum"
help = """
Photoalbum

Client to manage your photos.
"""

cli = Typer(name="photoalbum", help=help, epilog=epilog)


@cli.command(name="run")
def run():
    """
    Run the photoalbum client
    """
    print("Running photoalbum")

@cli.command(name="validate")
def validate_files():
    """
    Validate the files.
    """
    print("validate files")

if __name__ == "__main__":
    try:
        cli()
    except Exception as error:
        print("Something went wrong => %s", error)
