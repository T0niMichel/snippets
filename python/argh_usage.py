#!/usr/bin/python3

"""
# how to use argh

## installation
pip install argh
"""

from argh import ArghParser
from argh.decorators import aliases, arg

@arg('-m', '--evenmorestupid', help='make this function more stupid')
@aliases('s')
def stupid_function(evenmorestupid=False):
    if evenmorestupid:
      print('huh?')
    else:
      print('oh wow, i am a stupid function')


if __name__ == "__main__":
    parser = ArghParser()
    parser.add_commands([stupid_function])
    parser.dispatch()
