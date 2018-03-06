#!/bin/env python3
import click

@click.command()
@click.argument('name')
@click.option('--greetfrom', '-f', default="admin", 
              help="Who is greeting the person")
@click.option('--how', '-h', default="Hello", 
              help="How to greet the person")
def greet(name, greetfrom, how):
    """
    This script will greet person with [NAME] politely
    """
    print("{} {} from {}".format(how, name, greetfrom))
    
if __name__ == "__main__":
    greet()
