#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, line):
        return True
    def help_quit(self):
        print ('Quit command to exit the program\n')
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()