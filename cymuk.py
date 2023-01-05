from modules.cli_args import parser
from modules.keyboard_listener import listener, set_verbose as kl_sv
from modules.script_handler import parse_script, set_verbose as sh_sv


def main():
    args = vars(parser.parse_args())

    if (args["script"] != None):
        if (args["verbose"]):
            kl_sv()
            sh_sv()
            print("Script mode")

        print(parse_script(args["script"]))

        return

    else:
        if (args["verbose"]):
            kl_sv()
            sh_sv()
            print("Capture mode")
        listener.start()
        listener.join()


if __name__ == "__main__":
    main()
