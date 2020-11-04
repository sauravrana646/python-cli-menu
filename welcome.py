from clint.textui import colored
from colorama import Fore, Back, Style
from pyfiglet import Figlet


def welcome(text):
    result = Figlet()
    return colored.cyan(result.renderText(text))
