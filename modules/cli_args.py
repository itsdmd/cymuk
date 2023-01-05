# Parse Arguments Passed to the Script from CLI

from argparse import ArgumentParser

parser = ArgumentParser(prog="cymuk",
                        description="Control Your Mouse Using Keyboard")

parser.add_argument("-s", "--script",
                    action="store",
                    nargs="?")

parser.add_argument("-v", "--verbose",
                    action="store_true")
