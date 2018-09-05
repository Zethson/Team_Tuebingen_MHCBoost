import logging
import os

import click

from src.folder_1.test_src import some_function

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("test_src")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


@click.group()
@click.option(
    '-v', '--verbose',
    is_flag=True,
    default=False,
    help="Verbose output (print debug statements)"
)
def template(verbose):
    if verbose:
        LOG.debug("Verbose output enabled")
    else:
        LOG.debug("Verbose output disabled")


if __name__ == '__main__':
    print("""
___________                   .__          __          
\__    ___/___   _____ ______ |  | _____ _/  |_  ____  
  |    |_/ __ \ /     \\____ \|  | \__  \\   __\/ __ \ 
  |    |\  ___/|  Y Y  \  |_> >  |__/ __ \|  | \  ___/ 
  |____| \___  >__|_|  /   __/|____(____  /__|  \___  >
             \/      \/|__|             \/          \/ 
    """)
    some_function()
    template()
