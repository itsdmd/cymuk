from modules.cli_args import parser
from modules.keyboard_listener import listener
from modules.monitor import main as monitor
from modules.performer import centralize
from modules.script_handler import parse_script
import modules.global_properties as gp


def main():
    args = vars(parser.parse_args())

    if (args["verbose"]):
        gp.set_verbose()

    if (args["version"]):
        print("cymuk v{}".format(gp.get_version()))
        return

    if (args["script"] != None):
        if gp.verbose:
            print("Script mode")
            print(parse_script(args["script"]))
        return

    elif (args["mouse_position"]):
        if gp.verbose:
            print("Monitor mode. Ctrl+C to exit.")
        monitor()

    else:
        if gp.verbose:
            print("Capture mode")
        centralize()
        listener.start()
        listener.join()


if __name__ == "__main__":
    main()
