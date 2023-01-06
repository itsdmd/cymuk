from modules.cli_args import parser
from modules.config_handler import key_quit
from modules.keyboard_listener import listener
from modules.monitor import main as monitor
from modules.performer import centralize, quit
from modules.script_handler import parse_script
import modules.global_properties as gp


def main():
    gp.init()
    args = vars(parser.parse_args())

    if (args["verbose"]):
        gp.set_verbose()

    if (args["version"]):
        print("cymuk v{}".format(gp.get_version()))
        return

    if (args["capture"]) or len(args["script"]) == 0:
        if gp.get_verbose():
            print("Capture mode. {} to exit.".format(key_quit))
        centralize()
        listener.start()
        listener.join()

    elif (args["script"] != None):
        if gp.get_verbose():
            print("Script mode. Ctrl+C to cancel.")
            for i in range(len(args["script"])):
                print("Script {}: {}".format(i, args["script"][i]))
                print(parse_script(args["script"][i]))
                print("Finished parsing script {}".format(i))
        quit(0)

    elif (args["mouse_position"]):
        if gp.get_verbose():
            print("Monitor mode. Ctrl+C to exit.")
        monitor()


if __name__ == "__main__":
    main()
    quit(0)
