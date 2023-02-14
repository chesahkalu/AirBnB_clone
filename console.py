#!/usr/bin/python3
""" The Console """

import cmd
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    """The AirBnB console for command line interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exits console"""
        return True
    
    def emptyline(self):
        """No execution when an empty line is ENTERED"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
