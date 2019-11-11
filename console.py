#!/usr/bin/python3
""" HBNBCommand class """
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """I'm rich and this is my console
    Could you afford your own console?"""

    prompt = '(hbnb) '
    cls_arr = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City, "Place": Place,
               "Review": Review, "State": State, "User": User}

    def emptyline(self):
        """Empty line: Do nothing"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits cleanly at EOF"""
        return True

    def do_create(self, line):
        """ Creates an instance of a class """
        if line:
            if line in HBNBCommand.cls_arr:
                class_to_ins = HBNBCommand.cls_arr.get(line)
                new_inst = class_to_ins()
                # not working stuff to review
                new_inst.save()
                print(new_inst.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Prints the STR representation of an instance """
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        elif len(list_line) < 2:
            print("** instance id missing **")
        elif list_line[0] + '.' + list_line[1] not in models.storage.all().keys():
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
