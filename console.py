#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb)"

     def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
