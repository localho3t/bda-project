
from commands.basic_cmd import BasicCmd

class RenderCmd:


    bcmd = BasicCmd()
    def execute_command(self,command):
        commands = self.bcmd.commands()

        parts = command.split()
        cmd = parts[0]
        args = parts[1:]
        if cmd in commands:
            try:
                commands[cmd](*args)
            except TypeError:
                print(f"Command '{cmd}' takes no arguments")
        else:
            print(f"Unknown command: {cmd}")
    
    def get_flag(self):
        return self.bcmd.get_flag()