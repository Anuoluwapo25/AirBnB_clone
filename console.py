#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """

import cmd
from models.base_model import BaseModel
import sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True

    def help_EOF(self):
        """Prints help for the EOF command."""
        print("Quit command to exit the program")

    def do_quit(self, line):
        """Exit the program."""
        return True

    def help_quit(self):
        """Prints help for the quit command."""
        print('Quit command to exit the program')

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, class_name):
        """Create a new instance of the specified class."""
        if not class_name:
            print("** class name missing **")
            return

        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args or len(args) < 1:
            print('** class name missing **')
            return

        try:
            class_name = args[0]
            if class_name in globals():
                if len(args) > 1:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    objects = BaseModel.load_from_file()
                    if key in objects:
                        print(objects[key])
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        except NameError:
            print('** class doesn\'t exist **')

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        if not args or len(args) < 1:
            print('** class name missing **')
            return

        try:
            class_name = args[0]
            if class_name in globals():
                if len(args) > 1:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    objects = BaseModel.load_from_file()
                    if key in objects:
                        del objects[key]
                        BaseModel.save_to_file(objects)
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        except NameError:
            print('** class doesn\'t exist **')

    def do_all(self, arg):
        """Print string representation of all instances based on class name."""
        objects = BaseModel.load_from_file()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = arg
                print([str(obj) for key, obj in objects.items() if key.split('.')[0] == class_name])
            except NameError:
                print('** class doesn\'t exist **')

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = arg.split()
        if not args or len(args) < 1:
            print('** class name missing **')
            return

        try:
            class_name = args[0]
            if class_name in globals():
                if len(args) > 1:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    objects = BaseModel.load_from_file()
                    if key in objects:
                        if len(args) > 2:
                            attribute_name = args[2]
                            if len(args) > 3:
                                attribute_value = args[3].strip('"')
                                if hasattr(objects[key], attribute_name):
                                    setattr(objects[key], attribute_name, type(getattr(objects[key], attribute_name))(attribute_value))
                                    objects[key].save()
                                else:
                                    print('** attribute name missing **')
                            else:
                                print('** value missing **')
                        else:
                            print('** attribute name missing **')
                    else:
                        print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        except NameError:
            print('** class doesn\'t exist **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()

