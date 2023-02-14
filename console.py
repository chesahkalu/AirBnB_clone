#!/usr/bin/python3
""" The Console """

import cmd
from datetime import datetime
import shlex  # used with split to make any argument seperated by space a single token, also if quoted.
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"}

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

    def do_create(self, arg):
        """command: create <class>
        Creates a new instance of the given class"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = args[0]()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        """command: show <class> <id> 
        Prints a class instance string representation given the id"""
        args = shlex.split(arg)
        key = args[0] + "." + args[1]
        get_all = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif key not in get_all:
            print("** no instance found **")
        else:
            print(get_all[key])

    def do_destroy(self, arg):
        """command: destroy <class> <id>
        Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        key = args[0] + "." + args[1]
        get_all = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif key not in get_all:
            print("** no instance found **")
        else:
            del get_all[key]
            models.storage.save()

    def do_all(self, arg):
        """command: all <class> or all
        Prints all string representation of all instances based on the class name
        If no class is specified, displays all instantiated objects"""
        args = shlex.split(arg)
        o_list = []
        if args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    o_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(o_list), end="")
            print("]")
        elif len(args) == 0:
            for value in models.storage.all().values():
                o_list.append(str(value))
            print("[", end="")
            print(", ".join(o_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """command: count <class>
        Retrieve the number of instances of a given class."""    
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
