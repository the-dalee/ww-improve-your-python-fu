import click

@click.command()
@click.argument('name')
def greet(name):
    print(f"Hello {name}")
    
@click.command()
@click.argument('name')
def farawell(name):
    print(f"Goodbye {name}")

