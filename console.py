#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import sys


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True

    def help_EOF(self, command):
        print("EOF Command to exit the program\n")

    def do_quit(self, line):
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')

    def emptyline(self):
        pass

    def do_create(self, class_name):
        if class_name:
            if class_name in globals():
                basemodel_instance = BaseModel()

            else:
                print("** class doesn't exist **")

        elif not class_name:
            print("** class name missing **")

    def do_show(self, class_name):
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
