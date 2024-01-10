#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
        Defines the HBnB command interpreter

    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
    }


    def do_quit(self, arg):
        """ Quit command to exit the program 
        """
        return True


    def do_EOF(self, arg):
        """ EOF signal to exit the program 
        """
        print("")
        return True

    def emptyline(self):
        """ Do nothing when cmd erceive an empty line """
        pass

    def do_create(self, arg):
        """ Create command to create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
