import click

@click.command()
@click.option("--name", default="no_name", help="caller name")
def hello(name):
	click.echo(f"Hello {name}")
	

if __name__ == "__main__":
	hello()