#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb)"

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """

        if not line:
            print(** class name missing **)
        elif line not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        
        else:

    def do_show(self,line):

if __name__ == '__main__':
    HBNBCommand().cmdloop()
