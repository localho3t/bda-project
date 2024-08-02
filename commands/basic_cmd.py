import os
from commands.flag_mode import FlagMode


class BasicCmd(FlagMode):
    
    def commands(self):

        if self.get_flag() == 0:
            return {
                "say": self.__hi,
                "exit": lambda: exit(),
                "pwd": lambda: print(os.getcwd()),
                "ls": lambda: print("\n".join(os.listdir(os.getcwd()))),
                "set": self.__set_mode
            }
        elif self.get_flag() == 1:
            return {
                "mode" : lambda : print("![ basic mode ]!"),
                "exit" : self.exit__flag_mode,
                "quit" : self.exit__flag_mode,
            }

    def __hi(self, *args):
        if len(args) == 1:
            name = args[0]
            print(f"hi [{name}]")
        else:
            print("argv error !")

    def __set_mode(self, *args):
        if len(args) == 1:
            if args[0] == "basic":
                self.set_flag(1)
        else:
            print("argv error !")

    def get_flag(self):
        return self.flag_mode
    
    def exit__flag_mode(self):
        self.set_flag(0)