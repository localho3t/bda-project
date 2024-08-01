
from commands.basic_cmd import BasicCmd

class RenderCmd:
    def execute_command(self,command):
        bcmd = BasicCmd()
        commands = bcmd.commands

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