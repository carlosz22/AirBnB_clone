#!/usr/bin/python3
""" HBNBCommand class """
import cmd


class HBNBCommand(cmd.Cmd):
    """I'm rich and this is my console
    Could you afford your own console?"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Empty line: Do nothing"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits cleanly at EOF"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
