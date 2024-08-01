import os

class BasicCmd:

    def __init__(self):
        self.commands = {
            "say": self.__hi,
            "exit": lambda: exit(),
            "pwd": lambda: print(os.getcwd()),
            "ls": lambda: print("\n".join(os.listdir(os.getcwd())))
        }


    def __hi(self, *args):
        name = args[0]
        print(f"hi [{name}]")