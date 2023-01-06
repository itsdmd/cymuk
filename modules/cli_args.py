# Parse Arguments Passed To The Script From CLI

from argparse import ArgumentParser
from modules.config_handler import key_quit

parser = ArgumentParser(prog="cymuk",
                        description="Control Your Mouse Using Keyboard")

parser.add_argument("-c", "--capture",
                    action="store_true",
                    help="enter 'Capture' mode and start monitoring keyboard input; {} to exit".format(key_quit))

parser.add_argument("-s", "--script",
                    metavar="path/to/script",
                    action="extend",
                    nargs="*",
                    help="enter 'Script' mode and execute script files; separate multiple files with spaces; Ctrl+C to cancel")

parser.add_argument("-v", "--verbose",
                    action="store_true",
                    help="print debugging messages")

parser.add_argument("-V", "--version",
                    action="store_true",
                    help="print program version and exit")

parser.add_argument("-m", "--mouse-position",
                    action="store_true",
                    help="enter 'Monitor' mode and continuously print mouse cursor's position to the console; Ctrl+C to exit")
