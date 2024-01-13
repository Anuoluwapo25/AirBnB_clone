#!/usr/bin/python3
from cmd import Cmd

class HBNBCommand(Cmd):
    prompt = "(hbnb) "
    def do_quit(self, line):
        return True
    def help_quit(self):
        print ('Quit command to exit the program\n')
    def emptyline(self):
        pass
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()