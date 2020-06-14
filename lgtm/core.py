import click

@click.command()
def cli():
    """LGTM creating tool"""
    lgtm()
    click.echo('lgtm') 

def lgtm():
    pass