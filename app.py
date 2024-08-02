
from commands.render import RenderCmd

class main:



    def start(self):
        rcmd = RenderCmd()
        while True:
            try:
                flag_mode = rcmd.get_flag()
                if flag_mode == 0:
                    command = input("#~> ").strip()
                elif flag_mode == 1:
                    command = input("(basic mode) #~> ").strip()

                if command:
                    rcmd.execute_command(command)
            except KeyboardInterrupt:
                pass




if __name__ == "__main__":
    st = main()
    st.start()