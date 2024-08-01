
from commands.render import RenderCmd

def main():
    rcmd = RenderCmd()
    while True:
        try:
            command = input("myprompt> ").strip()
            if command:
                rcmd.execute_command(command)
        except KeyboardInterrupt:
            print("\nExiting...")
            break




if __name__ == "__main__":
    main()