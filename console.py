#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
from models.base_model import BaseModel
from models import storage

def deleteObjectById(id):
    """
    delete from file.json
    """
    try:
        with open("file.json", "r") as f:
            content = json.load(f)
        key_to_delete = []
        new_content = {k: v for k, v in content.items() if v.get("id") != id}
        if len(new_content) < len(content):
            with open("file.json", "w") as f:
                json.dump(new_content, f)
        return True
    except FileNotFoundError:
        return None


# read the file
def findObjectById(id):
    """
    read file.json file
    """
    try:
        with open("file.json", "r") as f:
            content = json.load(f)
            for k, v in content.items():
                # get the class name
                if id == v["id"]:
                    return eval(v["__class__"] + "(**v)")
    except FileNotFoundError:
        return None


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.
    """

    prompt = '(hbnb) '
    __classnames = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        arguments = arg.split()
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()

    def do_show(self, arg):
        arguments = arg.split()
        # search the id
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            my_model = findObjectById(arguments[1])
            if my_model is None:
                print("** no instance found **")
            else:
                print(my_model)

    def do_destroy(self, arg):
        arguments = arg.split()
        # search the id
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            # delete the my_model
            my_model = deleteObjectById(arguments[1])
            if my_model is None:
                print("** no instance found **")

    def do_all(self, arg):
        arguments = arg.split()
        list = []
        if len(arguments) >= 1:
            if arguments[0] not in self.__classnames:
                print("** class doesn't exist **")
            else:

                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    if obj_id == arguments[0]:
                        obj = all_objs[obj_id]
                        list.append(str(obj))
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                list.append(str(obj))
        print(list)

    def do_update(self, arg):
        arguments = arg.split()
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            my_model = findObjectById(arguments[1])
            if my_model is None:
                print("** no instance found **")
            elif len(arguments) < 3:
                print("** attribute name missing **")
            elif len(arguments) < 4:
                print("** value missing **")
            else:
                setattr(my_model, arguments[2], arguments[3])
                my_model.save()
                


if __name__ == '__main__':
    HBNBCommand().cmdloop()
