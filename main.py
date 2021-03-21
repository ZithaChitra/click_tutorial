import click


# @click.command()
# @click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name", help="Person to greet.")
# def hello(count, name):
# 	for x in range(count):
# 		click.echo("Hello %s!" % name)

@click.group()
def cli():
	pass


@click.command()
def initdb():
	click.echo("Initialized the database")


@click.command()
def dropdb():
	click.echo("Dropped the database")


cli.add_command(initdb)
cli.add_command(dropdb)



if __name__ == "__main__":
	cli()

