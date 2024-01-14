#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """

import cmd
from models.base_model import BaseModel
import sys


class HBNBCommand(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_

    Returns:
        _type_: _description_
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_

        Returns:
            _type_: _description_
        """
        print()
        return True

    def help_EOF(self):
        """_summary_
        """
        print("Quit command to exit the program")

    def do_quit(self, line):
        """_summary_

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        return True

    def help_quit(self):
        """_summary_
        """
        print('Quit command to exit the program')

    def emptyline(self):
        pass

    def do_create(self, class_name):
        """_summary_

        Args:
            class_name (_type_): _description_
        """
        if class_name:
            if class_name in globals():
                basemodel_instance = BaseModel()

            else:
                print("** class doesn't exist **")

        elif not class_name:
            print("** class name missing **")

    def do_show(self, class_name):
        """_summary_

        Args:
            class_name (_type_): _description_
        """
        if class_name:
            if class_name in globals():
                basemodel_instance = BaseModel()
            elif class_name.id is None:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

        elif not class_name:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
