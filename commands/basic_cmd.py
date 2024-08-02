import os
from commands.flag_mode import FlagMode
from apps.basic.read_file.app import ReadFile

class BasicCmd(FlagMode):
    
    rfile_class = ReadFile()
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
                "rfile" : self.rfile,
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

    def rfile(self, *args):
        if len(args) == 2:
            if args[0] == "--add" or args[0] == "-a":
                self.rfile_class.set_file_path(args[1])
           
        elif len(args) == 1:
            if args[0] == "--list" or args[0] == "-l":
                print(self.rfile_class.get_file_path())
            if args[0] == "--check" or args[0] == "-c":
                print(self.rfile_class.check_type_file())
            if args[0] == "--read-csv-data" or args[0] == "-rcd":
                self.rfile_class.read_csv()
            if args[0] == "--show-csv-data" or args[0] == "-scd":
                print(self.rfile_class.show_data())
        else:
            print("argv error !")
