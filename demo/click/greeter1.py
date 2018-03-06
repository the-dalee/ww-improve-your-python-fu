#!/bin/env python3
import click

@click.command()
@click.argument('greet_from')
@click.argument('greet_to')
def greet(greet_from, greet_to):
    """
    This script will greet you politely
    """
    print("Hello {} from {}".format(greet_to, greet_from))
    
if __name__ == "__main__":
    greet()
    
