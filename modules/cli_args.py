# Parse Arguments Passed To The Script From CLI

from argparse import ArgumentParser

parser = ArgumentParser(prog="cymuk",
                        description="Control Your Mouse Using Keyboard")

parser.add_argument("-s", "--script",
                    metavar="path/to/script",
                    action="store",
                    nargs="?",
                    help="enter 'Script' mode and execute a script file")

parser.add_argument("-v", "--verbose",
                    action="store_true",
                    help="print debugging messages")

parser.add_argument("-V", "--version",
                    action="store_true",
                    help="print program version and exit")

parser.add_argument("-m", "--mouse-position",
                    action="store_true",
                    help="enter 'Monitor' mode and continuously print mouse cursor's position to the console; Ctrl+C to exit")
