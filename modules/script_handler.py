# Read Automation Script

from modules.performer import fn_parser

verbose = False


def set_verbose():
    global verbose
    verbose = True


def parse_script(script_dir):
    with open(script_dir, "r") as script_file:
        script = script_file.read()
    line_num = 0
    for line in script.splitlines():
        args = line.split()
        try:
            args = args[:(args.index("//"))]
        except:
            pass
        if verbose:
            print("\nLine {}\nPerforming: {}".format(line_num, " ".join(args)))
        fn_parser(args[0], args[1:])
        line_num += 1
