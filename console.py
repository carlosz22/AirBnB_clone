#!/usr/bin/python3
""" HBNBCommand class """
import cmd
from models.base_model import BaseModel
from en
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
        if line == "":
            print("** class name missing **")





if __name__ == "__main__":
    HBNBCommand().cmdloop()
